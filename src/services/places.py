from typing import Optional

from src.clients.places import PlacesClient
from src.models.places import PlaceModel, UpdatePlaceModel


class PlacesService:
    """
    Сервис для работы с данными о любимых местах.
    """

    def get_place(self, place_id: int) -> Optional[PlaceModel]:
        """
        Получение объекта любимого места по его идентификатору.

        :return:
        """

        return PlacesClient().get_place(place_id)

    def get_places(
        self, limit: int, page: int, size: int
    ) -> Optional[list[PlaceModel]]:
        """
        Получение списка любимых мест.
        :param limit: Ограничение на количество объектов в выборке.
        :param page: Номер страницы.
        :param size: Количество элементов на странице.
        :return:
        """

        return PlacesClient().get_list(limit=limit, page=page, size=size)

    def create_place(self, place: PlaceModel) -> Optional[PlaceModel]:
        """
        Создание нового объекта любимого места.

        :param place: Объект любимого места для создания.
        :return:
        """

        return PlacesClient().create_place(place)

    def update_place(
        self, place_upd: UpdatePlaceModel
    ) -> Optional[UpdatePlaceModel]:
        return PlacesClient().update_place(place_upd)

    def delete_place(self, place_id: int) -> bool:
        """
        Удаление объекта любимого места по его идентификатору.

        :param place_id: Идентификатор объекта.
        :return:
        """

        return PlacesClient().delete_place(place_id)
