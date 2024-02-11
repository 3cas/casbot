CREATE TABLE users(
    uid INTEGER PRIMARY KEY NOT NULL;
    did INTEGER NOT NULL;
    rtime INTEGER NOT NULL;
    bank INTEGER NOT NULL DEFAULT 0;
    wallet INTEGER NOT NULL DEFAULT 0;
);

CREATE TABLE cooldowns(
    cid INTEGER PRIMARY KEY NOT NULL;
    start INTEGER NOT NULL;
    until INTEGER;
    name TEXT NOT NULL;
);

CREATE TABLE items(
    eid INTEGER PRIMARY KEY NOT NULL;
    type TEXT NOT NULL;
    ctime INTEGER NOT NULL;
    owner INTEGER;
    FOREIGN KEY(owner) REFERENCES users(did);
);

CREATE TABLE effects(
    eid INTEGER PRIMARY KEY NOT NULL;
    type type NOT NULL;
    until INTEGER;
    user INTEGER NOT NULL;
    FOREIGN KEY(user) REFERENCES users(did);
);

CREATE TABLE bans(
    bid INTEGER PRIMARY KEY NOT NULL;
    user INTEGER NOT NULL;
    time INTEGER NOT NULL;
    until INTEGER;
    reason TEXT NOT NULL;
    FOREIGN KEY(user) REFERENCES users(did);
);