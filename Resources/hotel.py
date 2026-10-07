from flask_restful import Resource, reqparse

hoteis = [
    {"hotel_id": "paraiso", "nome": "Hotel Paraiso Beach", "estrelas": 4.8, "diaria": 175, "cidade": "Lisboa"},
    {"hotel_id": "saint", "nome": "Hotel Saint Beach", "estrelas": 4.3, "diaria": 150, "cidade": "Coimbra"},
    {"hotel_id": "vila", "nome": "Hotel Vila Beach", "estrelas": 4.9, "diaria": 255, "cidade": "Vila do Conde"}
]

class Hoteis(Resource):
    def get(self):
        return {"hoteis": hoteis}

class Hotel(Resource):
    argumentos = reqparse.RequestParser()
    argumentos.add_argument("nome", type=str,required=True,help="1")
    argumentos.add_argument("estrelas", type=float,required=True,help="2")
    argumentos.add_argument("diaria", type=float,required=True,help="3")
    argumentos.add_argument("cidade", type=str,required=True,help="4")

    def encontrar_hotel(hotel_id):
        for hotel in hoteis:
            if hotel["hotel_id"] == hotel_id:
                return Hotel
        return None

    def get(self,hotel_id):
        hotel = self.encontrar_hotel(hotel_id)
        if hotel is None:
            return { "Mensagem": "Hotel não encontrado"}
        return hotel

    def post(self,hotel_id):
        hotel = self.encontrar_hotel(hotel_id)
            if hotel is not None:
                return { "mensagem": "Este hotel já existe"}

        dados = Hote.argumentos.parse_args()

        novo_hotel = {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 200
    def put(self,hotel_id):
        dados = Hotel.argumentos.parse_args()

        hotel = self.encontrar_hotel(hotel_id)
        if hotel is not None:
            hotel.update(dados)
            return hotel,200
        
        novo_hotel = {"hotel_id": hotel_id, **dados}
        hoteis.append(novo_hotel)
        return novo_hotel, 201
    
    def delete(self,hotel_id):
        global hoteis
        hoteis = [hotel for hotel in hoteis if hotel["hotel_id"] != hotel_id]
        return {"mensagem": f"Hotel com id {hotel_id} removido com sucesso"}
    