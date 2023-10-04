CREATE TYPE invoice_type AS ENUM ('Type1', 'Type2', 'Type3');

CREATE TABLE Invoices (
    id SERIAL PRIMARY KEY,
    type invoice_type,
    price FLOAT,
    quantity FLOAT
);
