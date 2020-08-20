# Banco-de-dados
## 1º Tarefa
### 1º Parte - Criar Tabelas
* Aluno:

~~~SQL
create table aluno(
matricula numeric(6),
nome varchar(200),
telefone numeric(10),
dtnascimento timestamp,
cidade varchar(100));
~~~

* Matricula:

~~~SQL
create table matricula(
matriculaaluno numeric(6),
coddisciplina numeric(6));
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
* Aluno 

~~~SQL
 create table aluno(
 matricula numeric(6),
 nome varchar(200),
 telefone numeric(10),
 dtnascimento timestamp,
 cidade varchar(100));

alter table aluno  add column email varchar(100);
alter table aluno add column idade numeric(3);
~~~
