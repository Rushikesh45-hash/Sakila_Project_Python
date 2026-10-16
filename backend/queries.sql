SELECT
    country.country,
    COUNT(address.address_id) AS addresscount
FROM country
INNER JOIN city
    ON country.country_id = city.country_id
INNER JOIN address
    ON city.city_id = address.city_id
GROUP BY 
    country.country
HAVING 
    addresscount > 4
ORDER BY 
    addresscount;