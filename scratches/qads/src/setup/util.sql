
CREATE PROCEDURE qads.pc_analyze_tables_like(IN schema_like VARCHAR(64),
                                                   IN table_like VARCHAR(64),
                                                   IN column_like VARCHAR(64))
BEGIN


	DECLARE done INTEGER DEFAULT 0;

	DECLARE cur_table_name VARCHAR(64);
	DECLARE cur_schema_name VARCHAR(64);

	DECLARE table_cursor
		CURSOR FOR
SELECT DISTINCT TABLE_SCHEMA, table_name
	FROM information_schema.tables
	     INNER JOIN information_schema.columns USING (TABLE_SCHEMA, TABLE_NAME)
	WHERE TABLE_SCHEMA LIKE schema_like
	  AND TABLE_NAME LIKE table_like
	  AND COLUMN_NAME LIKE column_like
	  AND TABLE_TYPE LIKE 'BASE TABLE';

DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

OPEN table_cursor;

get_table:
	LOOP

		FETCH table_cursor INTO cur_schema_name, cur_table_name;

		if done = 1 THEN
			LEAVE get_table;

END IF;


		SET @stmt = CONCAT('ANALYZE TABLE ', '`', cur_schema_name, '`', '.', '`', cur_table_name, '`');


PREPARE analises FROM @stmt;
EXECUTE analises;
DEALLOCATE PREPARE analises;


END LOOP get_table;


close table_cursor;


END
;
CREATE PROCEDURE qads.pc_optimize_tables_like(IN schema_like VARCHAR(64),
                                                    IN table_like VARCHAR(64),
                                                    IN column_like VARCHAR(64))
BEGIN


	DECLARE done INTEGER DEFAULT 0;

	DECLARE cur_table_name VARCHAR(64);
	DECLARE cur_schema_name VARCHAR(64);

	DECLARE table_cursor
		CURSOR FOR
		SELECT DISTINCT TABLE_SCHEMA, table_name
			FROM information_schema.tables
			     INNER JOIN information_schema.columns USING (TABLE_SCHEMA, TABLE_NAME)
			WHERE TABLE_SCHEMA LIKE schema_like
			  AND TABLE_NAME LIKE table_like
			  AND COLUMN_NAME LIKE column_like
			  AND TABLE_TYPE LIKE 'BASE TABLE';

	DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;

	OPEN table_cursor;

	get_table:
	LOOP

		FETCH table_cursor INTO cur_schema_name, cur_table_name;

		if done = 1 THEN
			LEAVE get_table;

		END IF;


		SET @stmt = CONCAT('OPTIMIZE TABLE ', '`', cur_schema_name, '`', '.', '`', cur_table_name, '`');


		PREPARE analises FROM @stmt;
		EXECUTE analises;
		DEALLOCATE PREPARE analises;


	END LOOP get_table;


	close table_cursor;


END
