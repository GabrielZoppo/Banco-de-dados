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
create table aluno (
	matricula int auto_increment,
	nome varchar (200),
	telefone int (10) unique,
	dtaNascimento timestamp,
	cidade varchar (100),
	email varchar(100) default 'Sem email',
	idade int (3),
 primary key(matricula)
);
  ~~~
  * matricula:
~~~SQL
use ucpel;
create table matricula(
 matricula_cod  numeric(6),
 cod_disciplina numeric(6),
 dtefetivado timestamp,
 primary key (matriculaaluno)
 foreign key (cod_disciplina) references disciplina (cod)
 );
~~~
* Disciplina:
 ~~~SQL
use ucpel;
create table disciplina(
 cod int auto_increment,
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
 cod int auto_increment,
 nome varchar(100),
 cargo varchar(100),
 salario numeric(10),
 departamento_cod numeric(6),
 dtcomntratacao timestamp,
 codgerente numeric(6),
 primary key (cod)
 );
 ~~~
 
 * Departamento:
~~~SQl
use ucpel;
create table departamento(
 cod int auto_increment,
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
select nome,salario from funcionario
where salario > 800;
~~~

* Crie uma consulta para exibir o nome do funcionário e o número do departamento para o código do funcionário 459
~~~SQL
select nome,coddepartamento from funcionario
where cod = 459;
~~~
* Exiba o nome e o salário de todos os funcionários cujos salários não estejam na faixa entre R$ 950,00 e R$ 2300,00
~~~SQL
select nome,salario from funcionario
where salario not between 950 and 2300;
~~~

### 2º Parte:
* Exiba o nome do funcionário, o cargo e a data dos funcionários admitidos entre 20 de fevereiro de 2004 e 1 de maio de 2007
~~~SQL
select nome,cargo,dtcomntratacao from funcionario
where dtcomntratacao between '2004-2-20' and '2007-5-1';
~~~
* Exiba o nome do funcionário e o número do departamento de todos os funcionários dos departamentos 10 e 30, por ordem alfabética de nome
~~~SQL
select nome,coddepartamento from funcionario
where coddepartamento = 10 and 30
order by nome;
~~~
* Liste o nome e o salário dos funcionários que recebem mais de R$ 1500,00 e que estão nos departamentos 10 ou 30. Nomeie as colunas Nome e Salário, para Funcionário e Salário do Mês
~~~SQL
select nome as funcionario,salario as salariodomes from funcionario
where salario > 1500 AND (coddepartamento= 10 OR coddepartamento= 30);
~~~
* Exiba o nome e a data de admissão de cada funcionário admitido em 2004
~~~SQL
select nome,dtcomntratacao from funcionario
where dtcomntratacao between '2004-1-1' and '2004-12-31';
~~~
### 3º Parte:
* Exiba o nome e o cargo de cada funcionário que não possua gerente
~~~SQL
select nome,cargo from funcionario
where codgerente is null;
~~~
* Exiba os nomes de todos os funcionários que possuem um A na segunda letra de seus nomes
~~~SQL
select nome from funcionario
where nome like '_A%';
~~~
* Exiba todos os funcionários que possuem duas letras A em seus nomes e estão no departamento 30 ou seu gerente seja o 7529, ordenado pelo código do departamento de forma decrescente
~~~SQL
select nome from funcionario
where nome like '%A%A%' and coddepartamento = 30 or codgerente = 7529
order by coddepartamento desc;
~~~
* Premie, aumentando o salário em R$ 300,00, de todos os funcionários que ganham menos de R$ 700,00
~~~SQL
SET SQL_SAFE_UPDATES = 0;
update funcionario
set salario = salario+300
where salario < 700;
~~~
* De um aumento de 15% aos funcionários do departamento 20
~~~SQL
SET SQL_SAFE_UPDATES = 0;
update funcionario
set salario = salario+(salario*(15/100))
where coddepartamento = 20;
~~~
## 4º Tarefa:
* Recriar a tabela aluno com chave primária e estrangeira
~~~SQL
CREATE TABLE aluno (
 matricula int(11) AUTO_INCREMENT NOT NULL,
 nome VARCHAR(200) DEFAULT NOT NULL, 
 telefone int(10) DEFAULT NULL,
 dtaNascimento timestamp DEFAULT NULL,
 cidade varchar(100) DEFAULT NULL,
 email varchar(100) DEFAULT NULL,
 idade decimal(3,0) DEFAULT NULL,
 PRIMARY KEY (matricula);

~~~
* Recriar a tabela matricula com chave primária e estrangeira
~~~SQL
create table matricula(
matriculaaluno numeric(6),
coddisciplina numeric(6),
dtefetivado timestamp,
primary key (matriculaaluno),
foreign key (coddisciplina) references disciplina(cod),

 );
~~~
* Recriar a tabela disciplina com chave primária e estrangeira
~~~SQL
use ucpel;
create table disciplina(
cod numeric(6) auto_increment,
nome varchar(100) DEFAULT NULL,
cargahoraria numeric(6) DEFAULT NULL,
numalunos numeric(6) DEFAULT NULL,
turma numeric(6) DEFAULT NULL,
primary key (cod)
);
~~~
* Recriar a tabela funcionário com chave primária e estrangeira
~~~SQL
create table funcionario(
cod numeric(6),
nome varchar(100),
cargo varchar(100),
salario numeric(10),
coddepartamento numeric(6),
dtcomntratacao timestamp,
codgerente numeric(6),
primary key (cod),
foreign key (coddepartamento) references departamento(cod),
foreign key (codgerente) references gerente(cod)
 );
~~~
* Recriar a tabela departamento com chave primária e estrangeira
~~~SQL
create table departamento(
 cod numeric(10),
 descricao varchar(500),
 sigla varchar(3) not null,
 primary key (cod)
 );
~~~
## 5º Tarefa:
### 1º Parte:
* Faça uma consulta que exiba o nome do funcionário e do departamento de todos os funcionários.
~~~SQL
select funcionario.nome,departamento.descricao
from funcionario
inner join departamento
on funcionario.coddepartamento = departamento.cod;
~~~

* Mostre todos os cargos dos funcionários lotados nos departamentos com sigla na CTB.
~~~SQL
select cargo from funcionario
inner join departamento
where departamento.sigla = "CTB"
~~~

* Mostre o número de alunos matriculados por disciplinas
~~~SQL
select matricula.coddisciplina,count(aluno.matricula) from matricula  
inner join aluno  
on matricula.matriculaaluno = aluno.matricula
group by matricula.coddisciplina
order by matricula.coddisciplina;
~~~

* Mostre o nome do funcionário e o nome do departamento dos funcionários que possuem um A em seus nomes.
~~~SQL
select funcionario.nome, departamento.descricao from funcionario 
left join departamento  
on funcionario.coddepartamento = departamento.cod
where funcionario.nome like "%A%";
~~~

* Faça uma consulta que retorne todos os funcionários que trabalham em departamentos situados no Rio de Janeiro e que o salario seja maior que R$ 1500,00.
~~~SQL
select funcionario.* from funcionario  
left join departamento  
on departamento.cod = funcionario.coddepartamento
where funcionario.salario > 1000.00 and departamento.sigla like "NS%";
~~~

* Retorne o nome do aluno e a carga de horas total das disciplinas que ele está matriculado. Ordene pelo nome do aluno.
~~~SQL
select aluno.nome,aluno.matricula,sum(disciplina.cargaHoraria) carga_total from aluno  
left join matricula  
on matricula.matriculaaluno = aluno.matricula 
left join disciplina  
on disciplina.cod = matricula.coddisciplina
group by aluno.nome;
~~~
 ### 2º Parte:
* Crie uma consulta para exibir o nome do departamento, a sigla, o número de funcionários e o salário médio de todos os funcionários neste departamento.
~~~SQL
SELECT departamento.descricao , departamento.sigla, count(funcionario.cod) n_func ,avg(funcionario.salario) media FROM departamento 
left join funcionario  on funcionario.coddepartamento = departamento.cod
group by departamento.cod;
~~~
* Monte uma consulta que informe a faixa salarial dos funcionários, de acordo com a tabela do slide 8. Em seguida faça um select com o número de funcionários por faixa salarial.
~~~SQL
~~~
* Crie uma tabela faixaNivel, onde os alunos com idade de 15 à 20 são nível A, 21 à 25 nível B, 25 à 30 nível C e acima nível D. Faça uma consulta retornando o nome do aluno e o nível em que ele se encontra.
~~~SQL
~~~
* Faça uma consulta para retornar todos os nomes de disciplinas e o número de alunos matriculados. Lembrando que se a disciplina não possuir aluno, deve informar 0 (zero).
~~~SQL
~~~
* Faça uma consulta para retornar o nome do aluno e a disciplina matriculada. Todos os alunos devem aparecer, mesmo se não estiver matriculado em nenhuma disciplina.
~~~SQL
~~~
### 3º Parte:
* Faça retornar o nome do gerente e o nome do funcionário O funcionario que não possuir gerente deve aparecer também.
~~~SQL
select funcionario.nome , gerente.nome from funcionario 
full JOIN gerente 
on funcionario.codgerente = gerente.id;
~~~
* Faça uma consulta que retorne os nomes dos funcionários e os nomes dos alunos, ordenados de forma decrescente. Os nomes duplicados devem aparecer
~~~SQL
select funcionario.nome,aluno.nome from funcionario 
full join aluno 
order by aluno.nome or funcionario.nome desc;
~~~
* A mesma consulta acima, sem duplicar nomes.

~~~SQL
~~~
* Faça retornar na mesma coluna o nome do aluno e o nome da disciplina sem repetições de nomes.
~~~SQL
select aluno.nome from aluno
full union
select disciplina.nome from disciplina;
~~~
* Faça um único select, que reproduzam os inserts existentes nas tabelas Funcionário e Aluno, gerando o resultado no formato de scripts para serem executados em outra base de dados.
~~~SQL

~~~

### 6º Tarefa:
* Crie uma consulta para exibir o nome e a data de admissão de todos os funcionários no mesmo departamento que Maria, excluindo Maria. Usando o IN
~~~SQL
select funcionario.nome, funcionario.dtcontrato from funcionario  
where funcionario.departamento_id = (select funcionario.departamento_id from funcionario  where funcionario.nome like 'Maria') 
and funcionario.nome in (select funcionario.nome from funcionario  where funcionario.nome <> 'Maria');
~~~

* Crie uma consulta para exibir o nome e a data de admissão de todos os funcionários no mesmo departamento que Maria, excluindo Maria. Usando EXISTS)
~~~SQL
select funcionario.nome, funcionario.dtcontrato from funcionario  
where funcionario.departamento_id = (select funcionario.departamento_id from funcionario  where funcionario.nome like 'Maria') 
and exists (select * from funcionario where funcionario.nome not like 'Maria');
~~~
* Crie uma consulta para exibir o código e o nome de todos os funcionários que recebem mais que o salário médio. Classifique os resultados, por salário, em ordem decrescente.
~~~SQL
select distinct(funcionario.cod),funcionario.nome, funcionario.salario,categoria_salario.categoria from funcionario ,categoria_salario 
where funcionario.salario < (select avg(funcionario.salario) from funcionario ) and funcionario.salario between categoria_salario.menor and categoria_salario.maior
order by funcionario.salario desc;
~~~
* Crie uma consulta que exiba o código e o nome de todos os funcionários que trabalhem em um departamento, onde exista um funcionário que possua a letra 'W' no nome.
~~~SQL
select funcionario.cod , funcionario.nome ,funcionario.departamento_id from funcionario  
where funcionario.departamento_id
in (select funcionario.departamento_id from funcionario  where funcionario.nome like '%E');
~~~
* Crie uma consulta para exibir o nome, a data de admissão e o salário de todos os funcionários que ganhem mais que a média de salário de todos os departamentos.
~~~SQL
select funcionario.nome , funcionario.cod, funcionario.salario from funcionario  
where funcionario.salario > (select avg(funcionario.salario) from funcionario );
~~~
* Selecione todos os gerentes que possuem efetivamente subordinados.
~~~SQL
select cod,nome from funcionario gerente
where exists (select 1 from funcionario  where funcionario.cod_gerente = gerente.cod);
~~~
* Selecione todos os colegas de 'MARIA' em todas as disciplinas que ela esta matriculada, de acordo com a “matricula” realizada na tabela aluno_disciplina. Usando o IN 
~~~SQL
select aluno.nome from aluno  right join matricula  on matricula.matricula_cod = aluno.matricula
where matricula.cod_disciplina in (select matricula.cod_disciplina from matricula left join aluno on aluno.matricula = matricula.matricula_cod where aluno.nome like 'Maria') and aluno.nome <> 'Maria'
group by a.matricula;
~~~

* Selecione todos os colegas de 'MARIA' em todas as disciplinas que ela esta matriculada, de acordo com a “matricula” realizada na tabela aluno_disciplina. Usando EXISTS
~~~SQL
select aluno.nome from aluno  right join matricula  on matricula.matricula_cod = aluno.matricula
where exists (select matricula.cod_disciplina from matricula  left join aluno aluno on aluno.matricula = matricula.matricula_cod where aluno.nome like 'Maria') and aluno.nome <> 'Maria'
group by aluno.nome;
~~~

