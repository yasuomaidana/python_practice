BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Users" (
	"name"	VARCHAR(128),
	"email"	VARCHAR(128)
);
INSERT INTO "Users" VALUES ('Chuck','csv@mail.com');
INSERT INTO "Users" VALUES ('Collen','co@mail.com');
INSERT INTO "Users" VALUES ('Yas','ya@mail.com');
INSERT INTO "Users" VALUES ('Nad','nad@mai.com');
INSERT INTO "Users" VALUES ('Ben','be@mail.com');
COMMIT;
