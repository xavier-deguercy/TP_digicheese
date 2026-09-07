CREATE TABLE IF NOT EXISTS `utilisateur` (
	`idUtil` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`nomUtil` VARCHAR NOT NULL,
	PRIMARY KEY(`idUtil`)
);


CREATE TABLE IF NOT EXISTS `role` (
	`idRole` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`libelleRole` VARCHAR NOT NULL,
	PRIMARY KEY(`idRole`)
);


CREATE TABLE IF NOT EXISTS `utilisateur_role` (
	`idUtilRole` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`idUtil` INT NOT NULL,
	`idRole` INT NOT NULL,
	PRIMARY KEY(`idUtilRole`)
) COMMENT='Table technique ajoutée pour matérialiser la relation n-n entre utilisateur et role.';


CREATE TABLE IF NOT EXISTS `commune` (
	`CP` VARCHAR NOT NULL UNIQUE,
	`Commune` VARCHAR NOT NULL,
	`Departement` VARCHAR NOT NULL,
	PRIMARY KEY(`CP`)
);


CREATE TABLE IF NOT EXISTS `adresse` (
	`idAdresse` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`compAdresse1` VARCHAR NOT NULL,
	`compAdresse2` VARCHAR,
	`compAdresse3` VARCHAR,
	`CP` VARCHAR NOT NULL,
	PRIMARY KEY(`idAdresse`)
);


CREATE TABLE IF NOT EXISTS `client` (
	`idClient` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`emailClient` VARCHAR NOT NULL UNIQUE,
	`idAdresse` INT NOT NULL,
	PRIMARY KEY(`idClient`)
);


CREATE TABLE IF NOT EXISTS `conditionnement` (
	`idCond` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`libelle` VARCHAR NOT NULL,
	`poidCondit` DECIMAL NOT NULL,
	`ordreImp` INT,
	PRIMARY KEY(`idCond`)
);


CREATE TABLE IF NOT EXISTS `commande` (
	`idCommande` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`date` DATE NOT NULL,
	`timbreClient` VARCHAR,
	`timbreCode` VARCHAR,
	`nbColis` INT,
	`bArchive` BOOLEAN NOT NULL,
	`idClient` INT NOT NULL,
	`idCond` INT,
	PRIMARY KEY(`idCommande`)
);


CREATE TABLE IF NOT EXISTS `objet` (
	`idObjet` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`libelle` VARCHAR NOT NULL,
	`taille` VARCHAR,
	`poids` DECIMAL,
	`bIndispo` BOOLEAN NOT NULL,
	PRIMARY KEY(`idObjet`)
);


CREATE TABLE IF NOT EXISTS `detail_commande` (
	`idDetailCommande` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`quantite` INT NOT NULL,
	`Colis` VARCHAR,
	`Commentaire` TEXT,
	`idCommande` INT NOT NULL,
	`idObjet` INT NOT NULL,
	PRIMARY KEY(`idDetailCommande`)
) COMMENT='Clé technique ajoutée pour faciliter l''implémentation relationnelle.';


CREATE TABLE IF NOT EXISTS `mise_a_jour` (
	`idMaj` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`quantiteMaj` INT NOT NULL,
	`dateMaj` DATE NOT NULL,
	`idObjet` INT NOT NULL,
	PRIMARY KEY(`idMaj`)
);


CREATE TABLE IF NOT EXISTS `prix` (
	`idPrix` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`prixObjet` DECIMAL NOT NULL,
	`idObjet` INT NOT NULL UNIQUE,
	PRIMARY KEY(`idPrix`)
) COMMENT='Modélisé ici en 1-1 avec objet via une FK unique.';


CREATE TABLE IF NOT EXISTS `stock` (
	`idStock` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`libelle` VARCHAR NOT NULL,
	PRIMARY KEY(`idStock`)
);


CREATE TABLE IF NOT EXISTS `stock_ligne` (
	`idStockLigne` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`libelle` VARCHAR,
	`dateDeb` DATE,
	`dateFin` DATE,
	`quantiteStock` INT NOT NULL,
	`idObjet` INT NOT NULL,
	`idStock` INT,
	PRIMARY KEY(`idStockLigne`)
);


CREATE TABLE IF NOT EXISTS `boutique` (
	`idBoutique` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`date` DATE,
	`quantiteBoutique` INT,
	`idObjet` INT NOT NULL,
	PRIMARY KEY(`idBoutique`)
);


CREATE TABLE IF NOT EXISTS `rel_cond` (
	`idRelCond` INT NOT NULL AUTO_INCREMENT UNIQUE,
	`quantiteObjet` INT NOT NULL,
	`idObjet` INT NOT NULL,
	`idCond` INT NOT NULL,
	PRIMARY KEY(`idRelCond`)
) COMMENT='Interprété comme table de relation entre objet et conditionnement.';


ALTER TABLE `utilisateur_role`
ADD FOREIGN KEY(`idUtil`) REFERENCES `utilisateur`(`idUtil`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `utilisateur_role`
ADD FOREIGN KEY(`idRole`) REFERENCES `role`(`idRole`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `adresse`
ADD FOREIGN KEY(`CP`) REFERENCES `commune`(`CP`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `client`
ADD FOREIGN KEY(`idAdresse`) REFERENCES `adresse`(`idAdresse`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `commande`
ADD FOREIGN KEY(`idClient`) REFERENCES `client`(`idClient`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `commande`
ADD FOREIGN KEY(`idCond`) REFERENCES `conditionnement`(`idCond`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `detail_commande`
ADD FOREIGN KEY(`idCommande`) REFERENCES `commande`(`idCommande`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `detail_commande`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `mise_a_jour`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `prix`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `stock_ligne`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `stock_ligne`
ADD FOREIGN KEY(`idStock`) REFERENCES `stock`(`idStock`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `boutique`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `rel_cond`
ADD FOREIGN KEY(`idObjet`) REFERENCES `objet`(`idObjet`)
ON UPDATE NO ACTION ON DELETE NO ACTION;
ALTER TABLE `rel_cond`
ADD FOREIGN KEY(`idCond`) REFERENCES `conditionnement`(`idCond`)
ON UPDATE NO ACTION ON DELETE NO ACTION;