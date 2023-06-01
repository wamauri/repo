function setAddButton() {
    $("#id_registro_versoes_button").removeClass("disabled")
    $("#id_tabela_button").removeClass("disabled")
    $("#id_querys_button").removeClass("disabled")
    $("#id_lgpd_button").removeClass("disabled")
    $("#id_abas_button").removeClass("disabled")
}

$("#createRepoForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/repos/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let repos = JSON.parse(resp)
            $("#createRepoForm").trigger("reset")
            $("#id_repos").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${repos["nome"]}</td>
                    <td class="text-xs align-middle text-nowrap">${repos["link"]}</td>
                    <td class="text-xs align-middle text-nowrap">31-05-2023 21:45:38</td>
                    <td class="text-xs align-middle text-nowrap">${repos["user_id"]}</td>
                    <td class="text-xs align-middle text-nowrap">${repos["publico_alvo"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-success btn-sm" target="_blank" href="${repos["link"]}" data-toggle="tooltip" data-placement="top" title="Abrir Dashboard">
                                    <i class="fas fa-share"></i>
                                </a>
                            </div>
                            <div class="mr-1">
                                <a class="btn btn-outline-secondary btn-sm" target="_blank" href="http://localhost:8501/?x=0&y=${repos["id"]}" data-toggle="tooltip" data-placement="top" title="Abrir Relatório">
                                    <i class="fas fa-share"></i>
                                </a>
                            </div>
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
            setAddButton()
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})

$("#createRegistroVersoesForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/registro_versoes_create/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let registroVersoesCreate = JSON.parse(resp)
            $("#createRegistroVersoesForm").trigger("reset")
            $("#id_registro_versoes").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${registroVersoesCreate["versao"]}</td>
                    <td class="text-xs align-middle text-nowrap">${registroVersoesCreate["responsavel"]}</td>
                    <td class="text-xs align-middle text-nowrap">${registroVersoesCreate["ticket"]}</td>
                    <td class="text-xs align-middle text-nowrap">${registroVersoesCreate["comentario"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})

$("#createLGPDForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/lgpd_create/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let LGPD = JSON.parse(resp)
            $("#createLGPDForm").trigger("reset")
            $("#id_lgpd").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${LGPD["nome_coluna"]}</td>
                    <td class="text-xs align-middle text-nowrap">${LGPD["conteudo_anonimizado"]}</td>
                    <td class="text-xs align-middle text-nowrap">${LGPD["justificativa_para_uso"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})

$("#createTabelasForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/tabelas_create/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let tabelas = JSON.parse(resp)
            $("#createTabelasForm").trigger("reset")
            $("#id_tabelas").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${tabelas["nome_tabela"]}</td>
                    <td class="text-xs align-middle text-nowrap">${tabelas["origem_dados"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})

$("#createAbasForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/abas_create/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let abas = JSON.parse(resp)
            $("#createAbasForm").trigger("reset")
            $("#id_abas").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${abas["nome"]}</td>
                    <td class="text-xs align-middle text-nowrap">${abas["descricao"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})

$("#createQuerysForm").on("submit", function(e) {
    e.preventDefault()
    let data = $(this).serialize()
    const csrfToken = document.getElementsByName("csrfmiddlewaretoken")[0].value

    $.ajax({
        url: "/querys_create/",
        type: "POST",
        data: data,
        dataType: "json",
        headers: {
            "X-Requested-With": "XMLHttpRequest",
            "X-CSRFToken": csrfToken
        },
        success: function(resp) {
            let querys = JSON.parse(resp)
            $("#createQuerysForm").trigger("reset")
            $("#id_querys").append(`
                <tr class="text-dark font-weight-bold">
                    <td class="text-xs align-middle text-nowrap">${querys["nome"]}</td>
                    <td class="text-xs align-middle text-nowrap text-break w-50">${querys["query"]}</td>
                    <td class="text-xs align-middle text-nowrap">${querys["tempo"]}</td>
                    <td class="text-xs align-middle text-nowrap">${querys["linhas"]}</td>
                    <td class="text-xs align-middle text-nowrap">${querys["colunas"]}</td>
                    <td class="text-xs align-middle">
                        <div class="row d-flex justify-content-center">
                            <div class="mr-1">
                                <a class="btn btn-outline-primary btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Editar">
                                    <i class="fas fa-pen-square"></i>
                                </a>
                            </div>
                            <div class="">
                                <a class="btn btn-outline-danger btn-sm" href="#" data-toggle="tooltip" data-placement="top" title="Deletar">
                                    <i class="fas fa-trash-alt"></i>
                                </a>
                            </div>
                        </div>
                    </td>
                </tr>
            `)
        },
        error: function() {
            console.log("Something went wrong!")
        }
    })
})