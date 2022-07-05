import sqlite3
connection = sqlite3.connect("goats.db")
cursor = connection.cursor()
try:
    table1 = 'CREATE TABLE "goats_table" ("ID"	INTEGER NOT NULL UNIQUE,"keci_id"	TEXT UNIQUE,"baba_id"	INTEGER,"anne_id"	INTEGER,"dogum_tarihi"	TEXT,"cinsiyeti"	TEXT,"cinsi"	INTEGER,"asim_zamani"	TEXT,PRIMARY KEY("ID" AUTOINCREMENT),FOREIGN KEY("cinsi") REFERENCES "types"("ID"),FOREIGN KEY("anne_id") REFERENCES "goats_table"("ID"),FOREIGN KEY("baba_id") REFERENCES "goats_table"("ID"))'
    table2 = 'CREATE TABLE "milk_efficency" ("ID"	INTEGER NOT NULL UNIQUE,"keci_id"	INTEGER NOT NULL,"kilo"	NUMERIC NOT NULL,"tarih"	TEXT NOT NULL,FOREIGN KEY("keci_id") REFERENCES "goats_table"("ID"),PRIMARY KEY("ID" AUTOINCREMENT))'
    table3 = 'CREATE TABLE "sick_report" (	"ID"	INTEGER NOT NULL UNIQUE,	"keci_id"	INTEGER NOT NULL,	"sick_id"	INTEGER NOT NULL,	"start_date"	TEXT NOT NULL,	"end_date"	TEXT,	PRIMARY KEY("ID" AUTOINCREMENT),	FOREIGN KEY("keci_id") REFERENCES "goats_table"("ID"),	FOREIGN KEY("sick_id") REFERENCES "sicks"("ID"))'
    table4 = 'CREATE TABLE "sicks" (	"ID"	INTEGER NOT NULL UNIQUE,	"sicks"	TEXT NOT NULL UNIQUE,	PRIMARY KEY("ID" AUTOINCREMENT))'
    table5 = 'CREATE TABLE "types" (	"ID"	INTEGER NOT NULL UNIQUE,"type"	TEXT NOT NULL UNIQUE,PRIMARY KEY("ID" AUTOINCREMENT))'
    table6 = 'CREATE TABLE "vaccine_report" ("ID"	INTEGER NOT NULL UNIQUE,	"keci_id"	INTEGER NOT NULL,	"asi_id"	INTEGER NOT NULL,	"tarih"	TEXT NOT NULL,	FOREIGN KEY("keci_id") REFERENCES "goats_table"("ID"),	FOREIGN KEY("asi_id") REFERENCES "vaccines"("ID"),	PRIMARY KEY("ID" AUTOINCREMENT))'
    table7 = 'CREATE TABLE "vaccines" (	"ID"	INTEGER NOT NULL UNIQUE,	"vaccines"	TEXT NOT NULL UNIQUE,	PRIMARY KEY("ID" AUTOINCREMENT))'
    table8 = 'CREATE TABLE "weight_report" (	"ID"	INTEGER NOT NULL UNIQUE,	"keci_id"	INTEGER NOT NULL,	"kilo"	NUMERIC NOT NULL,	"tarih"	TEXT NOT NULL,	FOREIGN KEY("keci_id") REFERENCES "goats_table"("ID"),	PRIMARY KEY("ID" AUTOINCREMENT))'
    table9 = 'CREATE TABLE "deleted_goats" (	"ID"	INTEGER NOT NULL UNIQUE,	"keci_id"	TEXT UNIQUE,	"baba_id"	INTEGER,	"anne_id"	INTEGER,	"dogum_tarihi"	TEXT,	"cinsiyeti"	TEXT,	"cinsi"	INTEGER,	"asim_zamani"	TEXT,	"delete_reason"	TEXT NOT NULL,	"delete_date"	TEXT NOT NULL,	FOREIGN KEY("anne_id") REFERENCES "goats_table"("ID"),	FOREIGN KEY("cinsi") REFERENCES "types"("ID"),	FOREIGN KEY("baba_id") REFERENCES "goats_table"("ID"),	PRIMARY KEY("ID" AUTOINCREMENT))'
    cursor.execute(table1)
    cursor.execute(table2)
    cursor.execute(table3)
    cursor.execute(table4)
    cursor.execute(table5)
    cursor.execute(table6)
    cursor.execute(table7)
    cursor.execute(table8)
    cursor.execute(table9)
    connection.commit()
except:
    pass