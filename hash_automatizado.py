import hashlib

# Frases reais a serem testadas (na ordem)
frases = [
    "A primeira das instituições criadas pelo Pe. Roberto Sabóia de Medeiros foi a antiga Escola Superior de Administração de Negócios de São Paulo - ESAN/SP.",
    "A FEI é uma instituição vinculada estatutariamente à Companhia de Jesus",
    "Em 20 de janeiro de 1951 foi realizada a sessão solene da congregação para a Colação de Grau da primeira turma da Faculdade de Engenharia Industrial.",
    "A Capela Santo Inácio de Loyola foi construída no ano de 1978, em concreto aparente.",
    "Tendo como função principal a promoção do aprimoramento profissional no campo administrativo e tecnológico, o IECAT (Instituto de Especialização em Ciências Administrativas e Tecnológicas) foi criado em 1982",
    "Dentro de uma proposta de integração e de agregação de competências, visando a excelência de seus cursos, as instituições FEI, FCI e ESAN foram transformadas no Centro Universitário da FEI no ano de 2002.",
    "O Centro Universitário da FEI passou a fazer parte do seleto grupo que produz ciência no Brasil, quando a CAPES aprovou o primeiro curso de Mestrado em Engenharia Elétrica em 2005.",
    "Em 2016 foi realizada a primeira edição do congresso de inovação - Megatendências 2050.",
    "Em 2012 o Centro Universitário FEI celebrou 70 anos de história e de excelência na inovação e na formação de mais de 50 mil profissionais altamente qualificados para o setor empresarial, entre Administradores, Engenheiros e Cientistas da Computação.",
    "Em 1999 iniciam-se as atividades da FCI (Faculdade de Informática), como o curso de Ciência da Computação."
]

def gerar_hashes(texto):
    return (
        hashlib.sha256(texto.encode('utf-8')).hexdigest(),
        hashlib.md5(texto.encode('utf-8')).hexdigest()
    )

def analisar_arquivo(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = [linha.strip() for linha in f if linha.strip()]

    resultados = []
    for i in range(0, len(linhas), 3):
        frase_index = (i // 3)
        sha256_informado = linhas[i+1]
        md5_informado = linhas[i+2]
        frase = frases[frase_index]
        sha256_calc, md5_calc = gerar_hashes(frase)

        sha256_ok = sha256_calc == sha256_informado
        md5_ok = md5_calc == md5_informado

        if sha256_ok and md5_ok:
            resultados.append(f"Frase {frase_index+1}: Verdadeira")
        elif sha256_ok or md5_ok:
            resultados.append(f"Frase {frase_index+1}: Falsa (Apenas um dos hashes corresponde; pode haver pequenas alterações na frase original.)")
        else:
            resultados.append(f"Frase {frase_index+1}: Falsa (Os hashes calculados não correspondem; a frase pode conter alterações como espaços, acentos ou pontuação.)")

    return resultados

#Alterar caminho do arquivo txt
resultados = analisar_arquivo(r"C:\Users\enzos\Documents\Faculdade\Facul 8° Semestre\Segurança da Informacao\Labs Feitos\atv 2\Frases.txt")
for linha in resultados:
    print(linha)
