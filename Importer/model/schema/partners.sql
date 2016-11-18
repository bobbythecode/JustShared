drop table if exists partners;
create table partners (
  id integer primary key autoincrement,
  name text not null,
  slug text
  active integer default 1,
  spread_sheet_path text
  img_path text
);