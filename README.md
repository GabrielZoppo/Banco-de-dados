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
 
 ### 4ª Parte - Criando tabelas com chaves primárias
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
  ### 5ª Parte - Inserindo dados nas tabelas
  * Aluno
  ~~~SQL
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20181, 'Gabriel Harter Zoppo', 'Pelotas');
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20182, 'Guilherme Corrêa Carvalho', 'São Lourenço do Sul');
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20183, 'Guilherme Moura Baccarin', 'Pelotas');
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20184, 'Helena Garcia Tavares', 'Pelotas');
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20185, 'Icaro Gonçalves Siqueira', 'São Lourenço do Sul ');
  INSERT INTO aluno(matricula, nome, cidade)
  VALUES (20186, 'Matheus Gonçalves Stigger', 'São Lourenço do Sul');
 
  ~~~
