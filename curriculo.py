import streamlit as st

# Configuração da página
st.set_page_config(page_title="Currículo de [Seu Nome]", layout="wide")

# Estilos CSS para centralizar o conteúdo
st.markdown("""
    <style>
        /* Estilo para centralizar todo o conteúdo */
        .container {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            text-align: center;
            padding: 20px;
        }

        /* Estilo para a foto */
        .photo {
            width: 150px;
            height: 150px;
            object-fit: cover;
            border-radius: 50%; /* Deixa a foto redonda */
            margin-bottom: 20px;
            border: 4px solid #ddd; /* Adiciona uma borda para destaque */
        }

        /* Estilo para os títulos e seções */
        .section {
            width: 80%;
            margin-top: 20px;
            text-align: left;
        }

        /* Estilo para as listas e links */
        .links {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Centralizando o conteúdo da página
st.markdown('<div class="container">', unsafe_allow_html=True)

# Exibindo a foto do usuário sem o parâmetro class_
st.image("foto_perfil.png", width=150)  # Foto de perfil no formato PNG, substitua o caminho da foto se necessário

# Exibindo o nome e título abaixo da foto
st.title("Currículo de [Seu Nome]")
st.write("Desenvolvedor Junior | Python")
st.write("Aprendendo JavaScrit,SQL,SQLite.")
# Adicionando seções do currículo

# Seção de Resumo
st.header("Resumo Profissional")
st.markdown("""
Sou um desenvolvedor apaixonado por tecnologia, em busca da min primeira experiência em desenvolvimento de sistemas de software.
Tenho conhecimento basico em **Python** e **JavaScript**.
""")

# Seção de Experiência Profissional
st.header("Experiência Profissional")
st.markdown("""
**Em busca da primeira experiência profissional**.
""")

# Seção de Educação
st.header("Educação")
st.markdown("""** Ensino superior | E.E. Prof. Lysanias de Oliveira Campos| Conclusão: 2023
""")

# Seção de Habilidades Técnicas
st.header("Habilidades Técnicas")
st.markdown("""
- **Linguagens**: Python,JavaScript,SQLite  
- **Bancos de Dados**: SQLite 
""")

# Seção de Projetos e Realizações
st.header("Projetos e Realizações")
st.markdown("""
Nenhum no momento 
""")

# Seção de Idiomas
st.header("Idiomas")
st.markdown("""
- **Inglês**: Basico  
""")

# Seção de Cursos e Treinamentos
st.header("Cursos e Treinamentos")
st.markdown("""
- **1. Senai | Curso python | Conclusão 2024**\n
- **2. Ebac | JavaScript | Em andamento**
""")


# Seção de Contatos
st.header("Contatos")
st.markdown("""
- **Email**: [pedronico76@gmail.com]
- **LinkedIn**: [LinkedIn - Seu Nome](https://www.linkedin.com/in/seunome/)  
- **GitHub**: [GitHub - Seu Nome](https://github.com/seunome)  
 
""")

# Fechando a tag de centralização
st.markdown('</div>', unsafe_allow_html=True)