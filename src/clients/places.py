import json
from http.client import HTTPException
from typing import Optional
from urllib.parse import urlencode, urljoin

from src.clients.base.base import BaseClient
from src.models.places import PlaceModel, UpdatePlaceModel
from src.settings import settings


class PlacesClient(BaseClient):
    """
    Реализация функций для получения информации о любимых местах.
    """

    @property
    def base_url(self) -> str:
        return settings.service.favorite_places.base_url

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        endpoint = f"/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)

        if response := self._request(self.GET, url):
            if place_data := response.get("data"):
                return self.__build_model(place_data)

        return None

    def get_list(self, limit: int, page: int, size: int) -> Optional[list[PlaceModel]]:
        """
        Получение списка любимых мест.
        :param limit: Ограничение на количество объектов в выборке.
        :param page: Номер страницы.
        :param size: Количество элементов на странице.
        :return:
        """

        params = {
            "limit": limit,
            "page": page,
            "size": size,
        }

        endpoint = "/api/v1/places"
        url = urljoin(self.base_url, f"{endpoint}?{urlencode(params)}")
        if response := self._request(self.GET, url):
            return [self.__build_model(place) for place in response.get("items", [])]

        return None

    def create_place(self, place: PlaceModel) -> Optional[PlaceModel]:
        """
        Создание нового объекта любимого места.

        :param place: Объект любимого места для создания.
        :return:
        """

        endpoint = "/api/v1/places"
        url = urljoin(self.base_url, endpoint)
        if response := self._request(self.POST, url, body=place.dict()):
            if place_data := response.get("data"):
                return self.__build_model(place_data)

        return None

    def delete_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Удаление объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        endpoint = f"/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)
        result = True
        try:
            self._request(self.DELETE, url)
        except HTTPException:
            result = False

        return result

    def update_place(
        self, place_id: int, place: UpdatePlaceModel
    ) -> PlaceModel:
        """
        Обновление объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :param place: Объект любимого места для обновления.
        :return:
        """

        endpoint = f"/api/v1/places/{place_id}"
        url = urljoin(self.base_url, endpoint)

        # Отправка запроса
        response = self._request(self.PATCH, url, body=place.dict())

        if response:
            # Извлечение данных из ответа
            try:
                place_data = response.get("data")
            except json.JSONDecodeError:
                pass
                # return False, PlaceModel

            # Создание модели из полученных данных
            return self.__build_model(place_data)

        # return False, None
        pass

    @staticmethod
    def __build_model(data: dict) -> PlaceModel:
        """
        Формирование модели для DTO-объекта любимого места на основе полученных данных.

        :param data: Данные для создания DTO
        :return:
        """

        return PlaceModel(
            id=data.get("id"),
            latitude=data.get("latitude"),
            longitude=data.get("longitude"),
            description=data.get("description"),
            country=data.get("country"),
            city=data.get("city"),
            locality=data.get("locality"),
            created_at=data.get("created_at"),
            updated_at=data.get("updated_at"),
        )
