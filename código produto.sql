-- tabela cliente
create table Cliente (
codcliente int,
nomecliente varchar (255),
sexo varchar (10),
primary key(codcliente)
);

-- Tabela Pedido
create table Pedido (
codped int,
data timestamp,
codcliente int ,
primary key(codped),
FOREIGN KEY (codcliente) REFERENCES Cliente(codcliente)
);

-- Tabela Produto 
create table Produto (
codproduto int,
nomeproduto varchar(255),
primary key(codproduto)
);

-- Tabela Item
create table Item (
codped int,
codproduto int,
quantidade int ,
valorunidade float,
foreign key (codproduto) references produto(codproduto),
foreign key (codped) REFERENCES Pedido(codped)
);
