INSERT INTO clubs (name, city) VALUES
('Tora Wrocław', 'Wrocław'),
('Sakura Poznań', 'Poznań'),
('Budokan Kraków', 'Kraków')
ON CONFLICT DO NOTHING;

INSERT INTO categories (code, name, min_age, max_age, min_weight, max_weight, gender) VALUES
('U18-70M', 'U18 do 70 kg (M)', 15, 18, NULL, 70, 'M'),
('SEN-OPEN', 'Senior Open (OPEN)', 18, NULL, NULL, NULL, 'OPEN')
ON CONFLICT DO NOTHING;
