from mercadopago import SDK

class Pagamento(object):
    def Pagamentos(self, hamburguer, preco_hamburguer):
        self.sdk = SDK("TEST-3407780045823713-121814-8b50879a9fb80c6cc27270dcdbe6bb5f-1276983227")

        self.preference_data = {
            "items": [
                {
                    "title": hamburguer,
                    "quantity": 1,
                    "unit_price": preco_hamburguer
                }
            ]
        }

        self.preference_response = self.sdk.preference().create(self.preference_data)
        self.preference = self.preference_response["response"]["init_point"]

        return self.preference