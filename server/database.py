# METADATA
__author__ = [
    'Henrique Kops',
    'José Goulart',
    'João Vieira',
    'João Etchichury',
    'Carlo José'
]
__date__ = '2019-08-30'
__version__ = '1.0'


class DBconnector:
    """Componente responsável pela persistência de dados"""

    _persistor = dict()

    @classmethod
    def show(cls):
        """Mostra todos os leilões ativos"""

        return cls._persistor

    @classmethod
    def bet(cls, product, price):
        """Aposta em um produto se ele existir"""
        try:
            price = float(price)
        except ValueError:
            return dict(
                message=f"'{price}' não é um preço válido!",
                submessage=f"Você precisa digitar apenas números. Utilize \
                    ponto ('.') para demarcar um número decimal"
            )
        except TypeError:
            return dict(
                message=f"É preciso de um preço para realizar o lance!",
                submessage=f"O preço do lance não pode ser vazio ou string."
            )
        
        bd_object = cls._persistor
        
        if product not in bd_object.keys():
            return dict(
                message="Esse produto nao existe!",
                submessage="Selecione algum produto nos leilões ativos"
            )
        
        elif price > int(bd_object.get(product)):
            bd_object.update({
                product: int(price)
            })
            return dict(
                message="Você está ganhando!",
                submessage=f"Agora o maior valor para {product} é de R${price}"
            )
        
        return dict(
            message=f"A sua aposta é baixa!",
            submessage=f"Faltam R${bd_object.get(product)-price+1} \
                para você poder apostar em {product}"
        )
    
    @classmethod
    def create(cls, product, price):
        """Insere um novo produto com um preço inicial"""
        try:
            price = float(price)
        except ValueError:
            return dict(
                message=f"{price} não é um preço válido.",
                submessage=f"Você precisa digitar apenas números. Utilize . \
                    (ponto) para demarcar um número decimal"
            )
        bd_object = cls._persistor
        
        if product not in bd_object.keys():
            bd_object.update({
                product: price
            })
        
            return dict(
                message="Leilão ativado!",
                submessage=f"Você cadastrou o produto {product} \
                    com preço inicial de R${price}!"
            )
            
        return dict(
            message="Falha ao adicionar este produto ao leilão!",
            submessage="Já existe um leilão para esse produto!"
        )

