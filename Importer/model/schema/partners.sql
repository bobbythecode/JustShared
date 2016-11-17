drop table if exists partners;
create table partners (
  id integer primary key autoincrement,
  name text not null,
  slug text
  spread_sheet_path text
  img_path text
);