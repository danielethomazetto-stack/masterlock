// =========================================================
// MASTERLOCK - PROTÓTIPO
// Reserva + WhatsApp funcionando
// =========================================================

document.addEventListener("DOMContentLoaded", () => {


    // =====================================================
    // CONFIGURAÇÃO
    // =====================================================

    const WHATSAPP_MASTERLOCK =
        "5569999287747";


    // =====================================================
    // ELEMENTOS
    // =====================================================

    const outroLocal =
        document.getElementById("outroLocal");

    const campoLocalDevolucao =
        document.getElementById("campoLocalDevolucao");

    const localRetirada =
        document.getElementById("localRetirada");

    const localDevolucao =
        document.getElementById("localDevolucao");

    const dataRetirada =
        document.getElementById("dataRetirada");

    const dataDevolucao =
        document.getElementById("dataDevolucao");

    const horaRetirada =
        document.getElementById("horaRetirada");

    const horaDevolucao =
        document.getElementById("horaDevolucao");

    const formBusca =
        document.getElementById("formBusca");

    const modalReserva =
        document.getElementById("modalReserva");

    const modalSucesso =
        document.getElementById("modalSucesso");

    const fecharReserva =
        document.getElementById("fecharReserva");

    const fecharSucesso =
        document.getElementById("fecharSucesso");

    const formReserva =
        document.getElementById("formReserva");

    const modalImagem =
        document.getElementById("modalImagem");

    const modalGrupo =
        document.getElementById("modalGrupo");

    const modalNome =
        document.getElementById("modalNome");

    const resumoRetirada =
        document.getElementById("resumoRetirada");

    const resumoDevolucao =
        document.getElementById("resumoDevolucao");

    const resumoDias =
        document.getElementById("resumoDias");

    const resumoTotal =
        document.getElementById("resumoTotal");

    const protocoloReserva =
        document.getElementById("protocoloReserva");

    const btnWhatsAppReserva =
        document.getElementById("btnWhatsAppReserva");

    const btnWhatsAppContato =
        document.getElementById("btnWhatsAppContato");

    const mobileMenu =
        document.getElementById("mobileMenu");

    const nav =
        document.getElementById("nav");

    const btnProposta =
        document.getElementById("btnProposta");

    const btnAreaCliente =
        document.getElementById("btnAreaCliente");


    let veiculoSelecionado = null;


    // =====================================================
    // DATA MÍNIMA
    // =====================================================

    const hoje =
        new Date();

    const hojeFormatado =
        hoje.toISOString().split("T")[0];


    if (dataRetirada) {
        dataRetirada.min =
            hojeFormatado;
    }

    if (dataDevolucao) {
        dataDevolucao.min =
            hojeFormatado;
    }


    // =====================================================
    // OUTRA UNIDADE
    // =====================================================

    if (outroLocal) {

        outroLocal.addEventListener(
            "change",
            () => {

                campoLocalDevolucao.classList.toggle(
                    "hidden",
                    !outroLocal.checked
                );

            }
        );

    }


    // =====================================================
    // DATA RETIRADA
    // =====================================================

    if (dataRetirada) {

        dataRetirada.addEventListener(
            "change",
            () => {

                dataDevolucao.min =
                    dataRetirada.value;


                if (
                    dataDevolucao.value &&
                    dataDevolucao.value <
                    dataRetirada.value
                ) {

                    dataDevolucao.value =
                        dataRetirada.value;

                }

            }
        );

    }


    // =====================================================
    // FORMATAR MOEDA
    // =====================================================

    function moeda(valor) {

        return Number(valor).toLocaleString(
            "pt-BR",
            {
                style: "currency",
                currency: "BRL"
            }
        );

    }


    // =====================================================
    // FORMATAR DATA
    // =====================================================

    function formatarData(data) {

        if (!data) {
            return "-";
        }


        const partes =
            data.split("-");


        return `${partes[2]}/${partes[1]}/${partes[0]}`;

    }


    // =====================================================
    // CALCULAR DIÁRIAS
    // =====================================================

    function calcularDias() {

        if (
            !dataRetirada.value ||
            !dataDevolucao.value
        ) {

            return 1;

        }


        const retirada =
            new Date(
                `${dataRetirada.value}T${horaRetirada.value || "00:00"}`
            );


        const devolucao =
            new Date(
                `${dataDevolucao.value}T${horaDevolucao.value || "00:00"}`
            );


        const diferenca =
            devolucao - retirada;


        if (diferenca <= 0) {

            return 1;

        }


        const dias =
            Math.ceil(
                diferenca /
                (1000 * 60 * 60 * 24)
            );


        return Math.max(
            dias,
            1
        );

    }


    // =====================================================
    // DADOS DA LOCAÇÃO
    // =====================================================

    function obterDadosLocacao() {

        const retirada =
            localRetirada.value ||
            "A definir";


        let devolucao =
            retirada;


        if (
            outroLocal.checked &&
            localDevolucao.value
        ) {

            devolucao =
                localDevolucao.value;

        }


        return {

            localRetirada:
                retirada,

            localDevolucao:
                devolucao,

            dataRetirada:
                dataRetirada.value,

            dataDevolucao:
                dataDevolucao.value,

            horaRetirada:
                horaRetirada.value,

            horaDevolucao:
                horaDevolucao.value,

            dias:
                calcularDias()

        };

    }


    // =====================================================
    // ABRIR RESERVA
    // =====================================================

    function abrirReserva(botao) {

        veiculoSelecionado = {

            grupo:
                botao.dataset.group,

            nome:
                botao.dataset.name,

            preco:
                Number(
                    botao.dataset.price
                ),

            imagem:
                botao.dataset.image

        };


        const locacao =
            obterDadosLocacao();


        const total =
            veiculoSelecionado.preco *
            locacao.dias;


        modalImagem.src =
            veiculoSelecionado.imagem;

        modalImagem.alt =
            veiculoSelecionado.nome;

        modalGrupo.textContent =
            `GRUPO ${veiculoSelecionado.grupo}`;

        modalNome.textContent =
            veiculoSelecionado.nome;


        resumoRetirada.textContent =
            locacao.dataRetirada
                ?
                `${locacao.localRetirada} • ${formatarData(locacao.dataRetirada)}`
                :
                locacao.localRetirada;


        resumoDevolucao.textContent =
            locacao.dataDevolucao
                ?
                `${locacao.localDevolucao} • ${formatarData(locacao.dataDevolucao)}`
                :
                locacao.localDevolucao;


        resumoDias.textContent =
            locacao.dias === 1
                ?
                "1 diária"
                :
                `${locacao.dias} diárias`;


        resumoTotal.textContent =
            moeda(total);


        modalReserva.classList.add(
            "active"
        );


        document.body.classList.add(
            "modal-open"
        );

    }


    // =====================================================
    // BOTÕES RESERVAR
    // =====================================================

    document
        .querySelectorAll(".reserve-button")
        .forEach(botao => {

            botao.addEventListener(
                "click",
                () => {

                    abrirReserva(
                        botao
                    );

                }
            );

        });


    // =====================================================
    // BUSCAR VEÍCULOS
    // =====================================================

    if (formBusca) {

        formBusca.addEventListener(
            "submit",
            event => {

                event.preventDefault();


                if (
                    !localRetirada.value ||
                    !dataRetirada.value ||
                    !dataDevolucao.value
                ) {

                    alert(
                        "Preencha o local e as datas da locação."
                    );

                    return;

                }


                document
                    .getElementById("frota")
                    .scrollIntoView({
                        behavior: "smooth"
                    });

            }
        );

    }


    // =====================================================
    // FILTROS
    // =====================================================

    const filtros =
        document.querySelectorAll(".filter");

    const cards =
        document.querySelectorAll(".fleet-card");


    filtros.forEach(filtro => {

        filtro.addEventListener(
            "click",
            () => {

                filtros.forEach(item => {

                    item.classList.remove(
                        "active"
                    );

                });


                filtro.classList.add(
                    "active"
                );


                const categoria =
                    filtro.dataset.filter;


                cards.forEach(card => {

                    if (
                        categoria === "todos" ||
                        card.dataset.category === categoria
                    ) {

                        card.classList.remove(
                            "filter-hidden"
                        );

                    } else {

                        card.classList.add(
                            "filter-hidden"
                        );

                    }

                });

            }
        );

    });


    // =====================================================
    // CRIAR MENSAGEM WHATSAPP
    // =====================================================

    function criarMensagemWhatsApp() {

        if (!veiculoSelecionado) {

            return "Olá! Gostaria de informações sobre locação de veículos da Masterlock.";

        }


        const locacao =
            obterDadosLocacao();


        const total =
            veiculoSelecionado.preco *
            locacao.dias;


        let mensagem =
`Olá! Gostaria de solicitar uma reserva na Masterlock.

Grupo: ${veiculoSelecionado.grupo}
Veículo: ${veiculoSelecionado.nome}

Retirada:
${locacao.localRetirada}
${formatarData(locacao.dataRetirada)} às ${locacao.horaRetirada || "-"}

Devolução:
${locacao.localDevolucao}
${formatarData(locacao.dataDevolucao)} às ${locacao.horaDevolucao || "-"}

Período: ${locacao.dias} diária(s)

Valor estimado: ${moeda(total)}

Gostaria de confirmar disponibilidade e condições.`;


        return mensagem;

    }


    // =====================================================
    // ABRIR WHATSAPP
    // =====================================================

    function abrirWhatsApp(mensagem) {

        const texto =
            encodeURIComponent(
                mensagem
            );


        const url =
            `https://wa.me/${WHATSAPP_MASTERLOCK}?text=${texto}`;


        window.open(
            url,
            "_blank"
        );

    }


    // =====================================================
    // WHATSAPP RESERVA
    // =====================================================

    if (btnWhatsAppReserva) {

        btnWhatsAppReserva.addEventListener(
            "click",
            () => {

                abrirWhatsApp(
                    criarMensagemWhatsApp()
                );

            }
        );

    }


    // =====================================================
    // WHATSAPP CONTATO
    // =====================================================

    if (btnWhatsAppContato) {

        btnWhatsAppContato.addEventListener(
            "click",
            event => {

                event.preventDefault();


                abrirWhatsApp(
                    "Olá! Gostaria de informações sobre locação de veículos e frotas da Masterlock."
                );

            }
        );

    }


    // =====================================================
    // CONFIRMAR RESERVA
    // =====================================================

    if (formReserva) {

        formReserva.addEventListener(
            "submit",
            event => {

                event.preventDefault();


                const nome =
                    document
                        .getElementById("clienteNome")
                        .value
                        .trim();


                const telefone =
                    document
                        .getElementById("clienteTelefone")
                        .value
                        .trim();


                if (
                    !nome ||
                    !telefone
                ) {

                    alert(
                        "Informe seu nome e WhatsApp."
                    );

                    return;

                }


                const pagamento =
                    document.querySelector(
                        'input[name="pagamento"]:checked'
                    ).value;


                const locacao =
                    obterDadosLocacao();


                const reserva = {

                    grupo:
                        veiculoSelecionado.grupo,

                    veiculo:
                        veiculoSelecionado.nome,

                    diaria:
                        veiculoSelecionado.preco,

                    local_retirada:
                        locacao.localRetirada,

                    local_devolucao:
                        locacao.localDevolucao,

                    data_retirada:
                        locacao.dataRetirada,

                    hora_retirada:
                        locacao.horaRetirada,

                    data_devolucao:
                        locacao.dataDevolucao,

                    hora_devolucao:
                        locacao.horaDevolucao,

                    dias:
                        locacao.dias,

                    cliente_nome:
                        nome,

                    cliente_whatsapp:
                        telefone,

                    forma_pagamento:
                        pagamento

                };


                reserva.valor_total =
                    reserva.diaria *
                    reserva.dias;


                console.log(
                    "Reserva pronta para banco:",
                    reserva
                );


                // protocolo temporário
                const numero =
                    Math.floor(
                        100000 +
                        Math.random() *
                        900000
                    );


                protocoloReserva.textContent =
                    `MST-${numero}`;


                modalReserva.classList.remove(
                    "active"
                );


                modalSucesso.classList.add(
                    "active"
                );


                // abre WhatsApp automaticamente com resumo
                const mensagem =
`Olá! Meu nome é ${nome}.

Acabei de fazer uma solicitação de reserva pelo site da Masterlock.

Protocolo: MST-${numero}

Grupo: ${reserva.grupo}
Veículo: ${reserva.veiculo}

Retirada:
${reserva.local_retirada}
${formatarData(reserva.data_retirada)} às ${reserva.hora_retirada}

Devolução:
${reserva.local_devolucao}
${formatarData(reserva.data_devolucao)} às ${reserva.hora_devolucao}

Período: ${reserva.dias} diária(s)

Pagamento: ${reserva.forma_pagamento}

Valor estimado: ${moeda(reserva.valor_total)}

Gostaria de confirmar a disponibilidade.`;


                setTimeout(
                    () => {

                        abrirWhatsApp(
                            mensagem
                        );

                    },
                    700
                );


                formReserva.reset();

            }
        );

    }


    // =====================================================
    // FECHAR MODAIS
    // =====================================================

    if (fecharReserva) {

        fecharReserva.addEventListener(
            "click",
            () => {

                modalReserva.classList.remove(
                    "active"
                );

                document.body.classList.remove(
                    "modal-open"
                );

            }
        );

    }


    if (fecharSucesso) {

        fecharSucesso.addEventListener(
            "click",
            () => {

                modalSucesso.classList.remove(
                    "active"
                );

                document.body.classList.remove(
                    "modal-open"
                );

            }
        );

    }


    if (modalReserva) {

        modalReserva.addEventListener(
            "click",
            event => {

                if (
                    event.target ===
                    modalReserva
                ) {

                    modalReserva.classList.remove(
                        "active"
                    );

                    document.body.classList.remove(
                        "modal-open"
                    );

                }

            }
        );

    }


    if (modalSucesso) {

        modalSucesso.addEventListener(
            "click",
            event => {

                if (
                    event.target ===
                    modalSucesso
                ) {

                    modalSucesso.classList.remove(
                        "active"
                    );

                    document.body.classList.remove(
                        "modal-open"
                    );

                }

            }
        );

    }


    // =====================================================
    // PROPOSTA EMPRESARIAL
    // =====================================================

    if (btnProposta) {

        btnProposta.addEventListener(
            "click",
            () => {

                abrirWhatsApp(
                    "Olá! Gostaria de solicitar uma proposta empresarial de locação de veículos e frotas da Masterlock."
                );

            }
        );

    }


    // =====================================================
    // ÁREA DO CLIENTE
    // =====================================================

    if (btnAreaCliente) {

        btnAreaCliente.addEventListener(
            "click",
            () => {

                alert(
                    "A Área do Cliente será criada na próxima etapa."
                );

            }
        );

    }


    // =====================================================
    // MENU MOBILE
    // =====================================================

    if (
        mobileMenu &&
        nav
    ) {

        mobileMenu.addEventListener(
            "click",
            () => {

                nav.classList.toggle(
                    "active"
                );

            }
        );


        nav
            .querySelectorAll("a")
            .forEach(link => {

                link.addEventListener(
                    "click",
                    () => {

                        nav.classList.remove(
                            "active"
                        );

                    }
                );

            });

    }


});