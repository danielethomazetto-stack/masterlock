import random
from datetime import datetime

from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

from config import Config


app = Flask(
    __name__,
    static_folder="static",
    static_url_path="/static"
)

app.config.from_object(Config)

db = SQLAlchemy(app)


# =========================================================
# MODELOS
# =========================================================


class Unidade(db.Model):
    __tablename__ = "unidades"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    cidade = db.Column(
        db.String(100),
        nullable=False
    )

    estado = db.Column(
        db.String(2),
        nullable=False,
        default="RO"
    )

    endereco = db.Column(
        db.String(255)
    )

    telefone = db.Column(
        db.String(30)
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


class GrupoVeiculo(db.Model):
    __tablename__ = "grupos_veiculos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    codigo = db.Column(
        db.String(5),
        nullable=False,
        unique=True
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    descricao = db.Column(
        db.Text
    )

    categoria = db.Column(
        db.String(50)
    )

    valor_diaria = db.Column(
        db.Numeric(12, 2)
    )

    max_parcelas = db.Column(
        db.Integer,
        default=1
    )

    permite_pix = db.Column(
        db.Boolean,
        default=True
    )

    permite_cartao = db.Column(
        db.Boolean,
        default=True
    )

    permite_pagamento_retirada = db.Column(
        db.Boolean,
        default=True
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


class Veiculo(db.Model):
    __tablename__ = "veiculos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    grupo_id = db.Column(
        db.Integer,
        db.ForeignKey("grupos_veiculos.id"),
        nullable=False
    )

    unidade_id = db.Column(
        db.Integer,
        db.ForeignKey("unidades.id"),
        nullable=False
    )

    nome = db.Column(
        db.String(120),
        nullable=False
    )

    marca = db.Column(
        db.String(80)
    )

    modelo = db.Column(
        db.String(100)
    )

    ano = db.Column(
        db.Integer
    )

    placa = db.Column(
        db.String(20)
    )

    cor = db.Column(
        db.String(50)
    )

    combustivel = db.Column(
        db.String(50)
    )

    cambio = db.Column(
        db.String(30)
    )

    lugares = db.Column(
        db.Integer
    )

    valor_diaria = db.Column(
        db.Numeric(12, 2)
    )

    valor_semanal = db.Column(
        db.Numeric(12, 2)
    )

    valor_mensal = db.Column(
        db.Numeric(12, 2)
    )

    caucao = db.Column(
        db.Numeric(12, 2)
    )

    imagem = db.Column(
        db.String(255)
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="disponivel"
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


class Cliente(db.Model):
    __tablename__ = "clientes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    cpf_cnpj = db.Column(
        db.String(20)
    )

    email = db.Column(
        db.String(150)
    )

    telefone = db.Column(
        db.String(30),
        nullable=False
    )

    data_nascimento = db.Column(
        db.Date
    )

    cep = db.Column(
        db.String(10)
    )

    endereco = db.Column(
        db.String(200)
    )

    numero = db.Column(
        db.String(20)
    )

    complemento = db.Column(
        db.String(100)
    )

    bairro = db.Column(
        db.String(100)
    )

    cidade = db.Column(
        db.String(100)
    )

    estado = db.Column(
        db.String(2)
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


class Reserva(db.Model):
    __tablename__ = "reservas"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    protocolo = db.Column(
        db.String(30),
        nullable=False,
        unique=True
    )

    cliente_id = db.Column(
        db.Integer,
        db.ForeignKey("clientes.id"),
        nullable=False
    )

    grupo_id = db.Column(
        db.Integer,
        db.ForeignKey("grupos_veiculos.id"),
        nullable=False
    )

    veiculo_id = db.Column(
        db.Integer,
        db.ForeignKey("veiculos.id")
    )

    unidade_retirada_id = db.Column(
        db.Integer,
        db.ForeignKey("unidades.id"),
        nullable=False
    )

    unidade_devolucao_id = db.Column(
        db.Integer,
        db.ForeignKey("unidades.id"),
        nullable=False
    )

    data_retirada = db.Column(
        db.Date,
        nullable=False
    )

    hora_retirada = db.Column(
        db.Time,
        nullable=False
    )

    data_devolucao = db.Column(
        db.Date,
        nullable=False
    )

    hora_devolucao = db.Column(
        db.Time,
        nullable=False
    )

    quantidade_diarias = db.Column(
        db.Integer,
        nullable=False
    )

    valor_diaria = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    valor_total = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    forma_pagamento = db.Column(
        db.String(30)
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="pendente"
    )

    observacoes = db.Column(
        db.Text
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )

    atualizado_em = db.Column(
        db.DateTime
    )


class Pagamento(db.Model):
    __tablename__ = "pagamentos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    reserva_id = db.Column(
        db.Integer,
        db.ForeignKey("reservas.id"),
        nullable=False
    )

    forma_pagamento = db.Column(
        db.String(30),
        nullable=False
    )

    valor = db.Column(
        db.Numeric(12, 2),
        nullable=False
    )

    parcelas = db.Column(
        db.Integer,
        default=1
    )

    status = db.Column(
        db.String(30),
        nullable=False,
        default="pendente"
    )

    codigo_transacao = db.Column(
        db.String(150)
    )

    pago_em = db.Column(
        db.DateTime
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        default=datetime.utcnow
    )


# =========================================================
# FUNÇÕES
# =========================================================


def gerar_protocolo():
    while True:
        numero = random.randint(
            100000,
            999999
        )

        protocolo = f"MST-{numero}"

        existente = Reserva.query.filter_by(
            protocolo=protocolo
        ).first()

        if not existente:
            return protocolo


def buscar_unidade_por_texto(texto):
    if not texto:
        return None

    unidade = Unidade.query.filter(
        Unidade.nome.ilike(
            f"%{texto}%"
        )
    ).first()

    if unidade:
        return unidade

    unidade = Unidade.query.filter(
        Unidade.cidade.ilike(
            f"%{texto}%"
        )
    ).first()

    return unidade


# =========================================================
# SITE
# =========================================================


@app.route("/")
def index():
    return send_from_directory(
        ".",
        "index.html"
    )


# =========================================================
# TESTE DE CONEXÃO
# =========================================================


@app.route("/api/status")
def status():
    try:
        db.session.execute(
            db.text("SELECT 1")
        )

        return jsonify({
            "ok": True,
            "mensagem": "Masterlock conectado ao Neon PostgreSQL."
        })

    except Exception as erro:

        return jsonify({
            "ok": False,
            "erro": str(erro)
        }), 500


# =========================================================
# UNIDADES
# =========================================================


@app.route(
    "/api/unidades",
    methods=["GET"]
)
def listar_unidades():

    unidades = Unidade.query.filter_by(
        ativo=True
    ).order_by(
        Unidade.cidade
    ).all()

    resultado = []

    for unidade in unidades:

        resultado.append({
            "id": unidade.id,
            "nome": unidade.nome,
            "cidade": unidade.cidade,
            "estado": unidade.estado
        })

    return jsonify(
        resultado
    )


# =========================================================
# GRUPOS
# =========================================================


@app.route(
    "/api/grupos",
    methods=["GET"]
)
def listar_grupos():

    grupos = GrupoVeiculo.query.filter_by(
        ativo=True
    ).order_by(
        GrupoVeiculo.codigo
    ).all()

    resultado = []

    for grupo in grupos:

        resultado.append({
            "id": grupo.id,
            "codigo": grupo.codigo,
            "nome": grupo.nome,
            "categoria": grupo.categoria,
            "valor_diaria": float(
                grupo.valor_diaria or 0
            ),
            "max_parcelas": grupo.max_parcelas
        })

    return jsonify(
        resultado
    )


# =========================================================
# CRIAR RESERVA
# =========================================================


@app.route(
    "/api/reservas",
    methods=["POST"]
)
def criar_reserva():

    try:

        dados = request.get_json()

        if not dados:
            return jsonify({
                "ok": False,
                "erro": "Nenhum dado recebido."
            }), 400


        # =================================================
        # CAMPOS OBRIGATÓRIOS
        # =================================================

        obrigatorios = [
            "grupo",
            "cliente_nome",
            "cliente_whatsapp",
            "local_retirada",
            "local_devolucao",
            "data_retirada",
            "hora_retirada",
            "data_devolucao",
            "hora_devolucao",
            "dias",
            "forma_pagamento"
        ]


        for campo in obrigatorios:

            if not dados.get(campo):

                return jsonify({
                    "ok": False,
                    "erro": f"Campo obrigatório não informado: {campo}"
                }), 400


        # =================================================
        # GRUPO
        # =================================================

        grupo = GrupoVeiculo.query.filter_by(
            codigo=dados["grupo"],
            ativo=True
        ).first()


        if not grupo:

            return jsonify({
                "ok": False,
                "erro": "Grupo de veículo não encontrado."
            }), 404


        # =================================================
        # UNIDADES
        # =================================================

        unidade_retirada = buscar_unidade_por_texto(
            dados["local_retirada"]
        )


        unidade_devolucao = buscar_unidade_por_texto(
            dados["local_devolucao"]
        )


        if not unidade_retirada:

            return jsonify({
                "ok": False,
                "erro": "Unidade de retirada não encontrada."
            }), 404


        if not unidade_devolucao:

            return jsonify({
                "ok": False,
                "erro": "Unidade de devolução não encontrada."
            }), 404


        # =================================================
        # CLIENTE
        # =================================================

        telefone = (
            dados["cliente_whatsapp"]
            .strip()
        )


        cliente = Cliente.query.filter_by(
            telefone=telefone
        ).first()


        if not cliente:

            cliente = Cliente(
                nome=dados[
                    "cliente_nome"
                ].strip(),
                telefone=telefone
            )

            db.session.add(
                cliente
            )

            db.session.flush()

        else:

            cliente.nome = dados[
                "cliente_nome"
            ].strip()


        # =================================================
        # DATAS E HORÁRIOS
        # =================================================

        data_retirada = datetime.strptime(
            dados["data_retirada"],
            "%Y-%m-%d"
        ).date()


        data_devolucao = datetime.strptime(
            dados["data_devolucao"],
            "%Y-%m-%d"
        ).date()


        hora_retirada = datetime.strptime(
            dados["hora_retirada"],
            "%H:%M"
        ).time()


        hora_devolucao = datetime.strptime(
            dados["hora_devolucao"],
            "%H:%M"
        ).time()


        if data_devolucao < data_retirada:

            return jsonify({
                "ok": False,
                "erro": "A devolução não pode ser anterior à retirada."
            }), 400


        # =================================================
        # VALORES
        # =================================================

        quantidade_diarias = int(
            dados["dias"]
        )


        if quantidade_diarias < 1:
            quantidade_diarias = 1


        valor_diaria = float(
            grupo.valor_diaria or 0
        )


        valor_total = (
            valor_diaria *
            quantidade_diarias
        )


        # =================================================
        # RESERVA
        # =================================================

        protocolo = gerar_protocolo()


        reserva = Reserva(

            protocolo=protocolo,

            cliente_id=cliente.id,

            grupo_id=grupo.id,

            veiculo_id=None,

            unidade_retirada_id=
                unidade_retirada.id,

            unidade_devolucao_id=
                unidade_devolucao.id,

            data_retirada=
                data_retirada,

            hora_retirada=
                hora_retirada,

            data_devolucao=
                data_devolucao,

            hora_devolucao=
                hora_devolucao,

            quantidade_diarias=
                quantidade_diarias,

            valor_diaria=
                valor_diaria,

            valor_total=
                valor_total,

            forma_pagamento=
                dados[
                    "forma_pagamento"
                ],

            status="pendente"
        )


        db.session.add(
            reserva
        )

        db.session.flush()


        # =================================================
        # PAGAMENTO
        # =================================================

        pagamento = Pagamento(

            reserva_id=
                reserva.id,

            forma_pagamento=
                dados[
                    "forma_pagamento"
                ],

            valor=
                valor_total,

            parcelas=1,

            status="pendente"
        )


        db.session.add(
            pagamento
        )


        db.session.commit()


        # =================================================
        # RESPOSTA
        # =================================================

        return jsonify({

            "ok": True,

            "mensagem":
                "Reserva criada com sucesso.",

            "reserva": {

                "id":
                    reserva.id,

                "protocolo":
                    protocolo,

                "cliente":
                    cliente.nome,

                "grupo":
                    grupo.codigo,

                "grupo_nome":
                    grupo.nome,

                "valor_diaria":
                    valor_diaria,

                "quantidade_diarias":
                    quantidade_diarias,

                "valor_total":
                    valor_total,

                "status":
                    reserva.status
            }

        }), 201


    except ValueError as erro:

        db.session.rollback()

        return jsonify({
            "ok": False,
            "erro": f"Dado inválido: {str(erro)}"
        }), 400


    except Exception as erro:

        db.session.rollback()

        print(
            "ERRO AO CRIAR RESERVA:",
            erro
        )

        return jsonify({
            "ok": False,
            "erro": "Não foi possível criar a reserva.",
            "detalhes": str(erro)
        }), 500


# =========================================================
# LISTAR RESERVAS
# Temporariamente para teste.
# Depois ficará protegido pelo login administrativo.
# =========================================================


@app.route(
    "/api/reservas",
    methods=["GET"]
)
def listar_reservas():

    reservas = Reserva.query.order_by(
        Reserva.id.desc()
    ).limit(
        100
    ).all()


    resultado = []


    for reserva in reservas:

        cliente = Cliente.query.get(
            reserva.cliente_id
        )

        grupo = GrupoVeiculo.query.get(
            reserva.grupo_id
        )

        resultado.append({

            "id":
                reserva.id,

            "protocolo":
                reserva.protocolo,

            "cliente":
                cliente.nome
                if cliente
                else None,

            "telefone":
                cliente.telefone
                if cliente
                else None,

            "grupo":
                grupo.codigo
                if grupo
                else None,

            "grupo_nome":
                grupo.nome
                if grupo
                else None,

            "data_retirada":
                reserva.data_retirada.isoformat(),

            "data_devolucao":
                reserva.data_devolucao.isoformat(),

            "quantidade_diarias":
                reserva.quantidade_diarias,

            "valor_total":
                float(
                    reserva.valor_total
                ),

            "forma_pagamento":
                reserva.forma_pagamento,

            "status":
                reserva.status,

            "criado_em":
                reserva.criado_em.isoformat()
                if reserva.criado_em
                else None
        })


    return jsonify(
        resultado
    )


# =========================================================
# EXECUÇÃO LOCAL
# =========================================================


if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )