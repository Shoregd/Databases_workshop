SELECT [columns to select] FROM [table name]
  WHERE [conditions];
UPDATE [table_name] SET [column_name] = [new_value]
  WHERE [conditions];

INSERT INTO [table_name]
  ( [list of columns] )
  VALUES( [list of values] );


DELETE FROM [table_name] WHERE [conditions];

-- Or, delete all records (never do this!)
DELETE FROM [table_name];