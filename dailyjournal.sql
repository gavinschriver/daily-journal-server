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