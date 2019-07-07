create table activity
(
	rev_id INT
		primary key,
	comment TEXT,
	edit_summary TEXT,
	edit_type TEXT,
	paraphase TEXT
)
;

create table article
(
	id INTEGER not null
		primary key
		 autoincrement
		constraint article_edit_quality_article_id_fk
			references edit_quality (article_id),
	item_id INTEGER,
	item_title TEXT,
	label TEXT,
	category TEXT
)
;

create table contribution
(
	rev_id INT,
	parent_id INT,
	editor_id INT,
	article_id INT,
	rev_timestamp REAL
)
;

create table editor
(
	id INTEGER not null
		primary key
		 autoincrement,
	user_id INTEGER,
	user_name TEXT,
	user_group TEXT,
	user_editcount int,
	user_registration text
)
;

create table quality
(
	rev_id INT,
	prediction TEXT,
	itemquality_A REAL,
	itemquality_B REAL,
	itemquality_C REAL,
	itemquality_D REAL,
	itemquality_E REAL,
	js_distance REAL
)
;
