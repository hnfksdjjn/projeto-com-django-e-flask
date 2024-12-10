# projeto-com-django
# projeto de cadastro de funcionario com django e flask

Aqui está uma explicação abrangente do seu projeto, que envolve a criação de uma aplicação Django para gerenciar funcionários:

### **Descrição Geral do Projeto**

Este projeto tem como objetivo o desenvolvimento de um sistema de gestão de funcionários utilizando Django, um framework web de alto nível em Python. O sistema oferece funcionalidades para cadastrar, listar, editar, excluir e visualizar informações dos funcionários de uma empresa. Além disso, o administrador tem a capacidade de visualizar gráficos e relatórios sobre o quadro de funcionários, como distribuição de cargos e médias salariais, além de gerar relatórios em formato PDF.

### **Funcionalidades Principais**

1. **Cadastro de Funcionários:**
   - O sistema permite que os administradores cadastrem novos funcionários no banco de dados. Para cada funcionário, são coletadas informações como nome, cargo, salário e data de contratação.
   - O administrador pode acessar a interface de administração do Django para adicionar ou editar funcionários.
  
   - ![projeto funcionario](https://github.com/user-attachments/assets/c43077d9-f6aa-4833-be24-55b313554ddc)

2. **Listagem de Funcionários:**
   - Os administradores podem visualizar todos os funcionários cadastrados no sistema.
   - A lista de funcionários é exibida com informações relevantes, como nome, cargo e salário. A visualização pode ser personalizada e filtrada conforme necessário.
   - ![projeto funcionario 3](https://github.com/user-attachments/assets/2427e69a-4913-4bb2-b2c0-315d742ee1ac)


3. **Exclusão de Funcionários:**
   - O administrador tem permissão para excluir funcionários do sistema caso necessário. A exclusão é feita através da interface de administração do Django.

4. **Gráficos e Relatórios:**
   - O sistema gera gráficos dinâmicos para visualizar a distribuição de cargos entre os funcionários e calcular a média salarial da empresa.
   - O gráfico de distribuição de cargos é um gráfico de barras, enquanto o gráfico de média salarial apresenta uma visualização do salário médio de todos os funcionários.
   - As bibliotecas como `plotly` são usadas para gerar esses gráficos de forma interativa.

### **Tecnologias Utilizadas**

1. **Django Framework:**
   - O Django é utilizado para construir a aplicação web. Ele gerencia a criação do banco de dados, autenticação de usuários, rotas da aplicação e renderização de templates HTML.
   - A arquitetura de Model-View-Template (MVT) do Django facilita o gerenciamento de dados, a lógica de apresentação e a interação do usuário.

2. **SQLite:**
   - O banco de dados utilizado inicialmente é o SQLite, que é o banco de dados padrão do Django. Ele é leve e fácil de configurar para fins de desenvolvimento e testes.

3. **Plotly:**
   - Para a geração de gráficos interativos, a biblioteca `plotly` é utilizada. Ela permite criar gráficos como o de distribuição de cargos e a média salarial de forma visual e dinâmica.

4. **ReportLab:**
   - Para a geração de relatórios em PDF, utilizamos a biblioteca `reportlab`. Ela permite criar documentos PDF formatados com informações dos funcionários ou relatórios customizados.

5. **Bootstrap (Opcional):**
   - O Bootstrap pode ser utilizado para estilizar as páginas e garantir que o sistema tenha uma interface amigável e responsiva.

### **Arquitetura e Estrutura do Projeto**

- **Models (`models.py`):**
   - Define o modelo `Employee`, que representa as informações de cada funcionário na empresa, como nome, cargo, salário e data de contratação.

- **Views (`views.py`):**
   - As views são responsáveis por tratar as solicitações HTTP, interagir com os modelos e renderizar as respostas. 
   - Existem views para exibir a lista de funcionários, gerar gráficos, criar novos funcionários e gerar relatórios em PDF.

- **URLs (`urls.py`):**
   - Define as rotas do aplicativo, associando URLs às views correspondentes. Isso inclui URLs para a tela de cadastro de funcionários, visualização de dados e gráficos, e a geração de relatórios.

- **Admin (`admin.py`):**
   - A configuração do Django Admin permite que o administrador adicione, edite ou exclua funcionários diretamente pela interface administrativa do Django. O modelo `Employee` é registrado para aparecer no painel de administração.

- **Templates (`templates/`):**
   - Contém arquivos HTML que definem como as páginas web são renderizadas. Usamos o Django Template Language (DTL) para inserir dinamicamente as informações dos funcionários e os gráficos nas páginas.

- **Static Files (`static/`):**
   - Armazena arquivos como CSS, JavaScript e imagens que são utilizados na interface do usuário.

### **Fluxo de Funcionamento**

1. **Cadastro de Funcionários:**
   - O administrador acessa a interface do Django Admin e preenche um formulário com os dados do funcionário, como nome, cargo, salário e data de contratação. O sistema armazena esses dados no banco de dados.

2. **Visualização de Funcionários:**
   - O administrador pode visualizar a lista de todos os funcionários através de uma página da aplicação. O sistema exibe dados como nome, cargo e salário de forma organizada e pode ser filtrado por cargo ou nome.

3. **Exclusão de Funcionários:**
   - A exclusão de funcionários é feita diretamente na interface administrativa, onde o administrador pode remover funcionários específicos, caso necessário.

4. **Gráficos:**
   - O administrador pode acessar uma página com gráficos interativos que mostram a distribuição de cargos dos funcionários e a média salarial da empresa. Esses gráficos são gerados com os dados armazenados no banco de dados.
![projeto funcionario 4](https://github.com/user-attachments/assets/4f325637-b354-4762-96c1-e60d3652d871)


### **Conclusão**

Este projeto fornece uma solução eficiente e prática para gerenciar informações de funcionários dentro de uma organização. Ele permite que administradores adicionem, editem, excluam e visualizem funcionários, além de gerar relatórios e gráficos úteis. Utilizando Django, a plataforma é escalável e fácil de manter, e com a utilização de bibliotecas como `plotly` e `reportlab`, oferece funcionalidades ricas em visualizações de dados e geração de documentos.
