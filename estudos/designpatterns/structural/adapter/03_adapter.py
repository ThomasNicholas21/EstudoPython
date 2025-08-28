"""
Outra abordagem utilizando composição
"""


class DataService:
    def get_data(self):
        data_dict = {
            "data": [
                {
                    "id": 1,
                    "name": "John Doe",
                },
                {
                    "id": 2,
                    "name": "Jane Doe",
                },
            ],
            "status": "success",
            "message": "Data retrieved successfully",
            "code": 200,
            "pagination": {
                "total": 2,
                "current_page": 1,
                "per_page": 10,
                "last_page": 1,
                "from": 1,
                "to": 2,
            }
        }
        return data_dict


class DataAdapter:
    def __init__(self):
        self.data_service = DataService()

    def get_data(self):
        data_dict = self.data_service.get_data()
        return data_dict["data"]

    def get_pagination(self):
        data_dict = self.data_service.get_data()
        return data_dict["pagination"]


if __name__ == "__main__":
    adapter = DataAdapter()
    data = adapter.get_data()
    pagination = adapter.get_pagination()
    print(data)
    print(pagination)
