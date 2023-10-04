CREATE TABLE IF NOT EXISTS schema_version (
    id serial PRIMARY KEY,
    version integer NOT NULL,
    created_at timestamptz DEFAULT now()
);

INSERT INTO schema_version (version)
SELECT 0 WHERE NOT EXISTS (SELECT 1 FROM schema_version);
