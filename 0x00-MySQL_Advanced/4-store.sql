-- File: 4-store.sql
-- Task: Create a trigger that decreases the quantity of an item after a new order is added.

DELIMITER //

-- Create a trigger that is executed after a new row is inserted into the 'orders' table.
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
    -- Update the 'items' table by decreasing the quantity of the ordered item.
    UPDATE items
    SET quantity = quantity - NEW.number -- on each row insert in `orders` table, decrease the quantity of the item by the number of items ordered in the `orders` table.
    WHERE name = NEW.item_name; -- set the name of the item to be updated in the `orders` table to the name of the new item from the `orders` table.
END;
//

DELIMITER ;
