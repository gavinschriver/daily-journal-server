CREATE TABLE `Instructors` (
    `id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `first_name` TEXT NOT NULL,
    `last_name` TEXT NOT NULL,
    `expertise` TEXT NOT NULL
);

CREATE TABLE `Moods` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `label` TEXT NOT NULL
);

CREATE TABLE `Tags` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `subject` TEXT NOT NULL    
);

CREATE TABLE `Entries` (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	`date`  TEXT NOT NULL,
    `topics` TEXT NOT NULL,
    `entry` TEXT NOT NULL,
    `moodId` INT NOT NULL,
    `instructorId` INT NOT NULL,
	FOREIGN KEY(`moodId`) REFERENCES `Instructors`(`id`),
	FOREIGN KEY(`instructorId`) REFERENCES `Moods`(`id`)
);

CREATE TABLE 'EntriesTags' (
	`id`  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `tagId` INTEGER NOT NULL,
    `entryId` INTEGER NOT NULL,
    FOREIGN KEY(`tagId`) REFERENCES `Instructors`(`id`),
	FOREIGN KEY(`entryId`) REFERENCES `Moods`(`id`)
);

INSERT INTO Moods VALUES (null, "annoyed");
INSERT INTO Moods VALUES (null, "flabbergasted");
INSERT INTO Moods VALUES (null, "grokking");
INSERT INTO Moods VALUES (null, "cooked");
INSERT INTO Moods VALUES (null, "intrepid");

INSERT INTO Instructors VALUES (null, "Joe", "Blow", "Shmoing");
INSERT INTO Instructors VALUES (null, "Jimmy", "Dean", "Makin the sausage");
INSERT INTO Instructors VALUES (null, "Billy", "Williams", "Givin them the business");

INSERT INTO Entries VALUES (null, "2020-07-14", "growin and glowin", "we did great stuff today. i enjoyed it so so very much", 3, 1);
INSERT INTO Entries VALUES (null, "2020-08-24", "cant remember", "leanred how to slash tires safely", 1, 3);
INSERT INTO Entries VALUES (null, "2020-08-27", "showing up and showing out", "truly expanded my mind today wow", 1, 2);
INSERT INTO Entries VALUES (null, "2020-10-12", "", "ooooof last night i got TOO RAGING TO CHEERS", 4, 3);
INSERT INTO Entries VALUES (null, "2020-10-12", "raging more", "ooooof last night I STUDIED ReACT CLASS COMPONENTS", 2, 3);

INSERT INTO Tags (null, "rompin");
