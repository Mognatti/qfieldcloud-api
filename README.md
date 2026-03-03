# QFieldCloud - API

Esta API visa estabelecer uma comunicação funcional e eficiente com projetos QFieldCloud através do uso da SDK oficial do QFieldCLoud

## Entendendo o QFieldCloud

QFieldCloud é uma forma de gerenciar os projetos que utilizam dados geográficos para diversos fins, com ênfase no mapeamento.

### Usuários

Para interagir com o QFieldCloud através do SDK, é necessário um usuário registrado na plataforma. Cada usuário pode criar, modificar
e deletar projetos e organizações.

### Projetos

Projetos são o container de dados de dados dentro do QFieldCloud. Atente-se ao tamanho dos projetos:

- Limite recomentado: 2GB
- Limite máximo: 10GB

**Valores acima do limite máximo irão falhar no processamento**

### Colaboradores de projeto

Um colaborador de projeto é um usuário do QFieldCloud que foi convidado para contribuir em um projeto.
Cada projeto pode ter múltiplos colaboradores. Cada colaborador pode ser configurado como proprietário
ou como administrador do projeto, o que afeta suas funções e permissões. Caso o projeto seja de
propriedade de uma empresa, podemos adicionar times de pessoas como colaboradores.

### Organizações

Organizações são contas compartilhadas nas quais múltiplos usuários podem colaborar em diversos projetos
ao mesmo tempo. Os donos e administradores podem gerenciar o acesso de determinados projetos para determinados
membros específicos. Um usuário pode fazer parte de múltiplas organizações.

As organizações podem ter times para facilitar o gerenciamento de permissões da organização, algo que é gerenciado
pelos donos e adminstradores.

### Autenticação

É possível autenticar usando o sistema básico de usuário e senha, mas também é possível configurar um OpenID.
Para o acesso desta API ao QFieldCloud (rodando em uma instância local via Docker) foi criado um token permanente
para evitar o processo de precisar logar com frequência no sistema, o que iria expor credenciais por mais vezes.
Para isso, o seguinte comando foi usado:

```bash
docker compose run app python manage.py shell -c "
from qfieldcloud.core.models import Person
from qfieldcloud.authentication.models import AuthToken
user = Person.objects.get(username='admin')
token, created = AuthToken.objects.get_or_create(user=user, client_type='python-sdk')
print(token.key)
"
```

Este token gerado foi salvo no .env como `QFIELDCLOUD_TOKEN` e é usado para fazer as requisições da API como se fosse
o usuário admin em questão.

## Diferença entre Owner e Admin de projeto

Só o owner pode:

- Deletar o projeto
- Transferir ownership

Colaborador admin pode:

- Sincronizar via QField app
- Fazer upload/download de arquivos
- Gerenciar outros colaboradores
- Disparar jobs de repackaging
- Editar metadados do projeto

### Links úteis

- SDK docs: https://opengisch.github.io/qfieldcloud-sdk-python/
- SDK GitHub: https://github.com/opengisch/qfieldcloud-sdk-python
- REST API docs: https://docs.qfield.org/reference/qfieldcloud/api/
- Swagger interativo: https://app.qfield.cloud/docs/
- Exemplos de uso: https://opengisch.github.io/qfieldcloud-sdk-python/examples/

## Entendendo a API

O QFieldCloud já possui uma API embutida, então é possível realizar os processos através de requisições diretas.
Entretanto, também temos a possibilidade de usarmos o SDK voltado para desenvolvimento Python, o que gera maior controle
e aumenta as possibilidades da interação. o SDK também lida com alguns processos de forma mais simples, evitando
que o desenvolvedor precise se preocupar tais processos (montar os headers de autenticação, serializar/deserializar JSON,
tratar códigos de status HTTP, paginar resultados, fazer retry em falhas, lidar com uploads de arquivos binários, etc.)

As demais informações acerca da API serão documentadas conforme desenvolvimento
