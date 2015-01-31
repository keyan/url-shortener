drop table if exists urls;
create table urls (
    url_id integer primary key autoincrement,
    original_url text not null
);