"""
==========================================================================================================================================================

База данных (БД) -  это организованная структура, предназначенная 
                    для хранения, изменения и обраблтки взаимосвязанной 
                    информации, преимущественно больших объемов

   виды:

- иерархическая
- объектная и объектно-ориентированная

- реляционная
  (возможность построяения отношений между таблицами внутри БД)

- объектно-реляционная
- сетевая
- функциональная

- нереляционные (не имеют отношений м.у таблицами и состоят 
  из модели коллекции и модели документов в которых данные
  хранятся по типу ключ значение)


SQL - Structured Query Language
СУБД - система управления базами данных - это комплекс программных 
       средств, необходимых для создания структуры новой базы,
       ее наполнения, редактирования содержимого и отображения информации.

Реляционные СУБД: MySQL, ORACLE, PostgreSQL, MS SQL Server

Запросы могут быть: простыми и вложенными


===========================================================================================================================================================

                                  ОСНОВНЫЕ КОМАНДЫ по работе с БАЗАМИ ДАННЫХ!!!!: 

1) CREATE DATABASE name_of_database
 например: postgres=# CREATE DATABASE test1
    (создание БД)

2) ALTER DATABASE name1 RENAME TO name2
 например: postgres-# ALTER DATABASE test1 RENAME to test2
    (переименование ранее созданного БД)

3) DROP DATABASE name_of_database
  например: postgres-# DROP DATABASE test1
    (удаление ранее созданного БД)

4) Создание юзера с паролем:
  например: postgres=# CREATE USER test_user WITH PASSWORD 'test1';

5) Сделать роль юзера SUPERUSER:
  например: postgres=# ALTER ROLE test_user WITH SUPERUSER;

6) Наделение всех прав юзеру по отношению к БД:
  например: postgres-# GRANT ALL PRIVILEGES ON DATABASE name_of_database TO name_user

7) Создание БД с определенным оунером:
  например: postgres-# CREATE DATABASE name_of_database WITH OWNER name_user

8) Удаление юзера:
  например: postgres=# DROP USER my_user;


===========================================================================================================================================================

                                                ОПЕРАТОРЫ в PSQL !!!
больше: >
меньше: <
равно: =
не равно: !=
не равно: <>
больше или равно: >=
меньше или равно: <=

сложение: +
отнимать: -
деление: /
умножение: *
деление с остатком (вывод остатка от деления): %

===========================================================================================================================================================

                                                ОСНОВНЫЕ КОМАНДЫ PSQL !!!

1). \c
    (ПЕРЕКЛЮЧЕНИЕ МЕЖДУ БАЗАМИ ДАННЫХ!!!)
например:
postgres=# \c hello 
You are now connected to database "hello" as user "postgres".
-----------------------------------------------------------------------------------------------------------------------------------------------------------

2). \l
    (список баз данных)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

3). \d table_name
    (показ структуры таблицы)

 например:
postgres=# \d car
                                        Table "public.car"
     Column      |         Type          | Collation | Nullable |             Default             
-----------------+-----------------------+-----------+----------+---------------------------------
 id              | integer               |           | not null | nextval('car_id_seq'::regclass)
 brand           | character varying(50) |           | not null | 
 model           | character varying(50) |           | not null | 
 state           | condition             |           |          | 'new'::condition
 price           | money                 |           |          | 
 is_registered   | boolean               |           |          | true
 date_of_release | date                  |           |          | 
Indexes:
    "car_pkey" PRIMARY KEY, btree (id)
-----------------------------------------------------------------------------------------------------------------------------------------------------------

4). \dt 
    (лист связей)

 например:
postgres=# \dt
 List of relations
 Schema | Name | Type  |  Owner   
--------+------+-------+----------
 public | info | table | postgres
-----------------------------------------------------------------------------------------------------------------------------------------------------------

5). \s
    (показать историю действий)

 например:
postgres=# \s
-----------------------------------------------------------------------------------------------------------------------------------------------------------

6). \h
    (покажет все команды/выражения по которым можно получить справку)

 например:
postgres=# \h
Available help:
  ABORT                            ALTER SYSTEM                     CREATE FOREIGN DATA WRAPPER      CREATE USER MAPPING              DROP ROUTINE                     PREPARE
  ALTER AGGREGATE                  ALTER TABLE                      CREATE FOREIGN TABLE             CREATE VIEW                      DROP RULE                        PREPARE TRANSACTION
  ALTER COLLATION                  ALTER TABLESPACE                 CREATE FUNCTION                  DEALLOCATE                       DROP SCHEMA                      REASSIGN OWNED
  ALTER CONVERSION                 ALTER TEXT SEARCH CONFIGURATION  CREATE GROUP                     DECLARE                          DROP SEQUENCE                    REFRESH MATERIALIZED VIEW
  ALTER DATABASE                   ALTER TEXT SEARCH DICTIONARY     CREATE INDEX                     DELETE                           DROP SERVER                      REINDEX
  ALTER DEFAULT PRIVILEGES         ALTER TEXT SEARCH PARSER         CREATE LANGUAGE                  DISCARD                          DROP STATISTICS                  RELEASE SAVEPOINT
  ALTER DOMAIN                     ALTER TEXT SEARCH TEMPLATE       CREATE MATERIALIZED VIEW         DO                               DROP SUBSCRIPTION                RESET
  ALTER EVENT TRIGGER              ALTER TRIGGER                    CREATE OPERATOR                  DROP ACCESS METHOD               DROP TABLE                       REVOKE
  ALTER EXTENSION                  ALTER TYPE                       CREATE OPERATOR CLASS            DROP AGGREGATE                   DROP TABLESPACE                  ROLLBACK
  ALTER FOREIGN DATA WRAPPER       ALTER USER                       CREATE OPERATOR FAMILY           DROP CAST                        DROP TEXT SEARCH CONFIGURATION   ROLLBACK PREPARED
  ALTER FOREIGN TABLE              ALTER USER MAPPING               CREATE POLICY                    DROP COLLATION                   DROP TEXT SEARCH DICTIONARY      ROLLBACK TO SAVEPOINT
  ALTER FUNCTION                   ALTER VIEW                       CREATE PROCEDURE                 DROP CONVERSION                  DROP TEXT SEARCH PARSER          SAVEPOINT
  ALTER GROUP                      ANALYZE                          CREATE PUBLICATION               DROP DATABASE                    DROP TEXT SEARCH TEMPLATE        SECURITY LABEL
  ALTER INDEX                      BEGIN                            CREATE ROLE                      DROP DOMAIN                      DROP TRANSFORM                   SELECT
  ALTER LANGUAGE                   CALL                             CREATE RULE                      DROP EVENT TRIGGER               DROP TRIGGER                     SELECT INTO
  ALTER LARGE OBJECT               CHECKPOINT                       CREATE SCHEMA                    DROP EXTENSION                   DROP TYPE                        SET
  ALTER MATERIALIZED VIEW          CLOSE                            CREATE SEQUENCE                  DROP FOREIGN DATA WRAPPER        DROP USER                        SET CONSTRAINTS
  ALTER OPERATOR                   CLUSTER                          CREATE SERVER                    DROP FOREIGN TABLE               DROP USER MAPPING                SET ROLE
  ALTER OPERATOR CLASS             COMMENT                          CREATE STATISTICS                DROP FUNCTION                    DROP VIEW                        SET SESSION AUTHORIZATION
  ALTER OPERATOR FAMILY            COMMIT                           CREATE SUBSCRIPTION              DROP GROUP                       END                              SET TRANSACTION
  ALTER POLICY                     COMMIT PREPARED                  CREATE TABLE                     DROP INDEX                       EXECUTE                          SHOW
  ALTER PROCEDURE                  COPY                             CREATE TABLE AS                  DROP LANGUAGE                    EXPLAIN                          START TRANSACTION
  ALTER PUBLICATION                CREATE ACCESS METHOD             CREATE TABLESPACE                DROP MATERIALIZED VIEW           FETCH                            TABLE
  ALTER ROLE                       CREATE AGGREGATE                 CREATE TEXT SEARCH CONFIGURATION DROP OPERATOR                    GRANT                            TRUNCATE
  ALTER ROUTINE                    CREATE CAST                      CREATE TEXT SEARCH DICTIONARY    DROP OPERATOR CLASS              IMPORT FOREIGN SCHEMA            UNLISTEN
  ALTER RULE                       CREATE COLLATION                 CREATE TEXT SEARCH PARSER        DROP OPERATOR FAMILY             INSERT                           UPDATE
  ALTER SCHEMA                     CREATE CONVERSION                CREATE TEXT SEARCH TEMPLATE      DROP OWNED                       LISTEN                           VACUUM
  ALTER SEQUENCE                   CREATE DATABASE                  CREATE TRANSFORM                 DROP POLICY                      LOAD                             VALUES
  ALTER SERVER                     CREATE DOMAIN                    CREATE TRIGGER                   DROP PROCEDURE                   LOCK                             WITH
  ALTER STATISTICS                 CREATE EVENT TRIGGER             CREATE TYPE                      DROP PUBLICATION                 MOVE                             
  ALTER SUBSCRIPTION               CREATE EXTENSION                 CREATE USER                      DROP ROLE                        NOTIFY                           
postgres=# 
-----------------------------------------------------------------------------------------------------------------------------------------------------------

7). \h КОМАНДА
    (справка по конкретной команде)

 например:
postgres=# \h SELECT
Command:     SELECT
Description: retrieve rows from a table or view
Syntax:
[ WITH [ RECURSIVE ] with_query [, ...] ]
SELECT [ ALL | DISTINCT [ ON ( expression [, ...] ) ] ]
    [ * | expression [ [ AS ] output_name ] [, ...] ]
    [ FROM from_item [, ...] ]
    [ WHERE condition ]
    [ GROUP BY [ ALL | DISTINCT ] grouping_element [, ...] ]
    [ HAVING condition ]
    [ WINDOW window_name AS ( window_definition ) [, ...] ]
    [ { UNION | INTERSECT | EXCEPT } [ ALL | DISTINCT ] select ]
    [ ORDER BY expression [ ASC | DESC | USING operator ] [ NULLS { FIRST | LAST } ] [, ...] ]
    [ LIMIT { count | ALL } ]
    [ OFFSET start [ ROW | ROWS ] ]
    [ FETCH { FIRST | NEXT } [ count ] { ROW | ROWS } { ONLY | WITH TIES } ]
    [ FOR { UPDATE | NO KEY UPDATE | SHARE | KEY SHARE } [ OF table_name [, ...] ] [ NOWAIT | SKIP LOCKED ] [...] ]

where from_item can be one of:

    [ ONLY ] table_name [ * ] [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
                [ TABLESAMPLE sampling_method ( argument [, ...] ) [ REPEATABLE ( seed ) ] ]
    [ LATERAL ] ( select ) [ AS ] alias [ ( column_alias [, ...] ) ]
    with_query_name [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
    [ LATERAL ] function_name ( [ argument [, ...] ] )
                [ WITH ORDINALITY ] [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
    [ LATERAL ] function_name ( [ argument [, ...] ] ) [ AS ] alias ( column_definition [, ...] )
    [ LATERAL ] function_name ( [ argument [, ...] ] ) AS ( column_definition [, ...] )
    [ LATERAL ] ROWS FROM( function_name ( [ argument [, ...] ] ) [ AS ( column_definition [, ...] ) ] [, ...] )
                [ WITH ORDINALITY ] [ [ AS ] alias [ ( column_alias [, ...] ) ] ]
    from_item [ NATURAL ] join_type from_item [ ON join_condition | USING ( join_column [, ...] ) [ AS join_using_alias ] ]

and grouping_element can be one of:

    ( )
    expression
    ( expression [, ...] )
    ROLLUP ( { expression | ( expression [, ...] ) } [, ...] )
    CUBE ( { expression | ( expression [, ...] ) } [, ...] )
    GROUPING SETS ( grouping_element [, ...] )

and with_query is:

    with_query_name [ ( column_name [, ...] ) ] AS [ [ NOT ] MATERIALIZED ] ( select | values | insert | update | delete )
        [ SEARCH { BREADTH | DEPTH } FIRST BY column_name [, ...] SET search_seq_col_name ]
        [ CYCLE column_name [, ...] SET cycle_mark_col_name [ TO cycle_mark_value DEFAULT cycle_mark_default ] USING cycle_path_col_name ]

TABLE [ ONLY ] table_name [ * ]

URL: https://www.postgresql.org/docs/14/sql-select.html


8). \du
    (список ролей)
postgres-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

===========================================================================================================================================================
"""

"""
УСТАНОВКА

hello@hello-Extensa-215-51:~$ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
[sudo] password for hello: 
hello@hello-Extensa-215-51:~$ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
OK
hello@hello-Extensa-215-51:~$ sudo apt-get update
.............................................................................................................................................................
hello@hello-Extensa-215-51:~$ psql --help
psql is the PostgreSQL interactive terminal.

Usage:
  psql [OPTION]... [DBNAME [USERNAME]]

General options:
  -c, --command=COMMAND    run only single command (SQL or internal) and exit
  -d, --dbname=DBNAME      database name to connect to (default: "hello")
  -f, --file=FILENAME      execute commands from file, then exit
  -l, --list               list available databases, then exit
  -v, --set=, --variable=NAME=VALUE
                           set psql variable NAME to VALUE
                           (e.g., -v ON_ERROR_STOP=1)
  -V, --version            output version information, then exit
  -X, --no-psqlrc          do not read startup file (~/.psqlrc)
  -1 ("one"), --single-transaction
                           execute as a single transaction (if non-interactive)
  -?, --help[=options]     show this help, then exit
      --help=commands      list backslash commands, then exit
      --help=variables     list special variables, then exit

Input and output options:
  -a, --echo-all           echo all input from script
  -b, --echo-errors        echo failed commands
  -e, --echo-queries       echo commands sent to server
  -E, --echo-hidden        display queries that internal commands generate
  -L, --log-file=FILENAME  send session log to file
  -n, --no-readline        disable enhanced command line editing (readline)
  -o, --output=FILENAME    send query results to file (or |pipe)
  -q, --quiet              run quietly (no messages, only query output)
  -s, --single-step        single-step mode (confirm each query)
  -S, --single-line        single-line mode (end of line terminates SQL command)

Output format options:
  -A, --no-align           unaligned table output mode
      --csv                CSV (Comma-Separated Values) table output mode
  -F, --field-separator=STRING
                           field separator for unaligned output (default: "|")
  -H, --html               HTML table output mode
  -P, --pset=VAR[=ARG]     set printing option VAR to ARG (see \pset command)
  -R, --record-separator=STRING
                           record separator for unaligned output (default: newline)
  -t, --tuples-only        print rows only
  -T, --table-attr=TEXT    set HTML table tag attributes (e.g., width, border)
  -x, --expanded           turn on expanded table output
  -z, --field-separator-zero
                           set field separator for unaligned output to zero byte
  -0, --record-separator-zero
                           set record separator for unaligned output to zero byte

Connection options:
  -h, --host=HOSTNAME      database server host or socket directory (default: "/var/run/postgresql")
  -p, --port=PORT          database server port (default: "5432")
  -U, --username=USERNAME  database user name (default: "hello")
  -w, --no-password        never prompt for password
  -W, --password           force password prompt (should happen automatically)

For more information, type "\?" (for internal commands) or "\help" (for SQL
commands) from within psql, or consult the psql section in the PostgreSQL
documentation.

Report bugs to <pgsql-bugs@lists.postgresql.org>.
PostgreSQL home page: <https://www.postgresql.org/>
................................................................................................................................................
hello@hello-Extensa-215-51:~$ sudo -i -u postgres
postgres@hello-Extensa-215-51:~$ psql
psql (14.0 (Ubuntu 14.0-1.pgdg20.04+1))
Type "help" for help.
................................................................................................................................................
postgres=# create database tesr;
CREATE DATABASE
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 tesr      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
(4 rows)
................................................................................................................................................
postgres=# alter database tesr rename to test;
ALTER DATABASE
................................................................................................................................................
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 test      | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
(4 rows)
................................................................................................................................................
postgres=# drop database test;
DROP DATABASE
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(3 rows)

postgres-# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}

................................................................................................................................................
postgres=# create user test_user with password 'test1';
CREATE ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 test_user |                                                            | {}
................................................................................................................................................

postgres=# alter role test_user with superuser;
ALTER ROLE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 test_user | Superuser
................................................................................................................................................

postgres=# create database my_db_test_user with owner test_user;
CREATE DATABASE
postgres=# \l
                                      List of databases
      Name       |   Owner   | Encoding |   Collate   |    Ctype    |   Access privileges    
-----------------+-----------+----------+-------------+-------------+------------------------
 hello           | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 my_db           | test_user | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 my_db_test_user | test_user | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres        | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0       | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
                 |           |          |             |             | postgres=CTc/postgres
 template1       | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres           +
                 |           |          |             |             | postgres=CTc/postgres
 test_user       | postgres  | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =Tc/postgres          +
                 |           |          |             |             | postgres=CTc/postgres +
                 |           |          |             |             | test_user=CTc/postgres
(7 rows)
................................................................................................................................................

postgres=# drop user my_user;
DROP ROLE
postgres=# \l
                                  List of databases
   Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
 hello     | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 my_user   | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | 
 template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
           |          |          |             |             | postgres=CTc/postgres
(5 rows)
................................................................................................................................................

postgres=# drop database my_user;
DROP DATABASE
postgres=# \du
                                   List of roles
 Role name |                         Attributes                         | Member of 
-----------+------------------------------------------------------------+-----------
 hello     | Superuser, Create role, Create DB                          | {}
 postgres  | Superuser, Create role, Create DB, Replication, Bypass RLS | {}
 test_user | Superuser, Create role, Create DB                          | {}

................................................................................................................................................

"""

