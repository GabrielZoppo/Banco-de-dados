# Banco-de-dados
## Parte Teórica:
* [Google Drive](https://drive.google.com/drive/u/1/folders/1qL9prTNtKDThsiQJQvh7YzlO1sDxZ1sa)
* [Teoria SQL](https://www.w3schools.com/sql/default.asp)
## 1º Tarefa
### 1º Parte - Criar Tabelas
* Aluno:

~~~SQL
create table aluno(
matricula numeric(6),
nome varchar(200),
telefone numeric(10),
dtnascimento timestamp,
cidade varchar(100)
);
~~~

* Matricula:

~~~SQL
create table matricula(
matriculaaluno numeric(6),
coddisciplina numeric(6)
);
~~~

* Disciplina:

~~~SQL
create table disciplina(
cod numeric(6),
nome varchar(100),
cargahoraria numeric(6)
);
~~~

* Funcionário:
~~~SQL
create table funcionario(
cod numeric(6),
nome varchar(100),
cargo varchar(100),
salario numeric(10),
coddepartamento numeric(6)
);
~~~

* Departamento
~~~SQL
create table departamento(
cod numeric(6),
descricao varchar(500)
);
~~~

### 2º Parte - Alterar tabelas
* Aluno: 

~~~SQL
 create table aluno(
 matricula numeric(6),
 nome varchar(200),
 telefone numeric(10),
 dtnascimento timestamp,
 cidade varchar(100)
 );
alter table aluno  add column email varchar(100);
alter table aluno add column idade numeric(3);
~~~

* Matricula:
~~~SQl
create table matricula(
 matriculaaluno numeric(6),
 coddisciplina numeric(6)
 );
 alter table matricula add column dtefetivado timestamp;
 ~~~
 
 * Disciplina:
~~~SQl
create table disciplina(
 cod numeric(6),
 nome varchar(100),
 cargahoraria numeric(6)
 );
alter table disciplina add column numalunos numeric(6);
alter table disciplina add column turma numeric(6);
 ~~~
 * Funcionário:
~~~SQl
create table funcionario(
 cod numeric(6),
 nome varchar(100),
 cargo varchar(100),
 salario numeric(10),
 coddepartamento numeric(6)
 );
alter table funcionario add column dtcomntratacao timestamp;
alter table funcionario add column codgerente numeric(6);
 ~~~
 * Departamento:
~~~SQl
 create table departamento(
 cod numeric(6),
 descricao varchar(500)
 );
alter table departamento add column sigla varchar(10);
 ~~~
 
 ### 3º Parte - Dropar as tabelas
 ~~~SQL
 DROP DATABASE ucpel;
 ~~~
 
 ## 2º Tarefa:
 ### 1ª Parte - Criando tabelas com chaves primárias
 * Aluno:
 ~~~SQL
use ucpel;
create table aluno(
 matricula numeric(6),
 nome varchar(200),
 telefone numeric(10),
 dtnascimento timestamp,
 cidade varchar(100),
 email varchar(100),
 idade numeric(3),
 primary key (matricula)
 );
  ~~~
  * matricula:
~~~SQL
use ucpel;
create table matricula(
 matriculaaluno numeric(6),
 coddisciplina numeric(6),
 dtefetivado timestamp,
 primary key (matriculaaluno,coddisciplina)
 );
~~~
* Disciplina:
 ~~~SQL
use ucpel;
create table disciplina(
 cod numeric(6),
 nome varchar(100),
 cargahoraria numeric(6),
 numalunos numeric(6),
 turma numeric(6),
 primary key (cod)
 );
  ~~~
  * Funcionário:
~~~SQl
use ucpel;
create table funcionario(
 cod numeric(6),
 nome varchar(100),
 cargo varchar(100),
 salario numeric(10),
 coddepartamento numeric(6),
 dtcomntratacao timestamp,
 codgerente numeric(6),
 primary key (cod)
 );
 ~~~
 
 * Departamento:
~~~SQl
use ucpel;
create table departamento(
 cod numeric(6),
 descricao varchar(500),
 sigla varchar(10),
 primary key (cod)
 );
 ~~~
### 2º parte Seleções - Projeções
* Selecione todos os registros das tabelas Funcionario
~~~SQl
SELECT * FROM ucpel.funcionario;
~~~
* Selecione somente a matricula e o nome dos registros da tabela Aluno
~~~SQl
SELECT matricula,nome FROM ucpel.aluno;
~~~
* Na tabela Funcionario, selecione o código, o nome, o salario atual e o salário atual + 10 %, colocando o apelido/alias nesta ultima coluna de “novosalario”
~~~SQl
SELECT cod,salario,salario+0.1 as novosalario FROM ucpel.funcionario;
~~~
* Selecione a coluna sigla na tabela Departamento, sem repetir registros iguais.
~~~SQl
SELECT DISTINCT sigla FROM ucpel.departamento;
~~~
* Selecione a descricao e a sigla na tabela Departamento, sem repetir registros iguais. Apelide a coluna descricao de “nomedepartamento” e sigla de “codigoreduzido”
~~~SQl
SELECT DISTINCT sigla as codigoreduzido,descricao as nomedepartamento FROM ucpel.departamento;
~~~
* Selecione todas as idades dos alunos, sem repeti-las
~~~SQl
SELECT DISTINCT idade FROM ucpel.aluno;
~~~
* Selecione a matricula, o nome, a idade e a idade + 2 apelidando esta ultima coluna de “provavel_idade_formado”
~~~SQl
SELECT matricula,nome,idade,idade+2 as provavel_idade_formado FROM ucpel.aluno;
~~~
* Faça retornar o seguinte texto oriundo da tabela Aluno Aluno: xxxxxx nascido em: xxxxx estará com a idade aproximada de xx ao se formar!
~~~SQl
SELECT CONCAT("Aluno: ",nome,"nascido em: ",dtnascimento,"estara com idade aproximada de: ", idade+2) as frase from ucpel.aluno ;
~~~
## 3º Tarefa:
### 1º Etapa:
* Selecione todos os alunos que não possuem email ou telefone:
~~~SQL
select *
from aluno
where telefone is null or (email is null);
~~~
* atualize os alunos, aumentando um ano a idade dos alunos que nasceram depois de 01/01/1980
~~~SQL
update aluno
set idade = idade+1
where dtnascimento>'1980-01-01';
~~~
* atualize as disciplinas, deixando todas com cargas horárias igual a 60
~~~SQL
update disciplina
set cargaHoraria = 60;
~~~
* Crie uma consulta para exibir o nome e o salário dos funcionários que recebem mais de R$ 800,00
~~~SQL

~~~

* Crie uma consulta para exibir o nome do funcionário e o número do departamento para o código do funcionário 459
~~~SQL

~~~
* Exiba o nome e o salário de todos os funcionários cujos salários não estejam na faixa entre R$ 950,00 e R$ 2300,00
~~~SQL

~~~

### 2º Parte:
* Exiba o nome do funcionário. o cargo e a data dos funcionários admitidos entre 20 de fevereiro de 2004 e 1 de maio de 2007
~~~SQL

~~~
* Exiba o nome do funcionário e o número do departamento de todos os funcionários dos departamentos 10 e 30, por ordem alfabética de nome
~~~SQL

~~~
* Liste o nome e o salário dos funcionários que recebem mais de R$ 1500,00 e que estão nos departamentos 10 ou 30. Nomeie as colunas Nome e Salário, para Funcionário e Salário do Mês
~~~SQL

~~~
* Exiba o nome e a data de admissão de cada funcionário admitido em 2004
~~~SQL

~~~
### 3º Parte:
* Exiba o nome e o cargo de cada funcionário que não possua gerente
~~~SQL

~~~
* Exiba os nomes de todos os funcionários que possuem um A na segunda letra de seus nomes
~~~SQL

~~~
* Exiba todos os funcionários que possuem duas letras A em seus nomes e estão no departamento 30 ou seu gerente seja o 7529, ordenado pelo código do departamento de forma decrescente
~~~SQL

~~~
* Premie, aumentando o salário em R$ 300,00, de todos os funcionários que ganham menos de R$ 700,00
~~~SQL

~~~
* De um aumento de 15% aos funcionários do departamento 20
~~~SQL

~~~
