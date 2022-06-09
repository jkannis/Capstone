CREATE TABLE "combined_data" 
AS
SELECT ar.*,
		re.latitude,
		re.longitude		
FROM
	public.arabica_ratings AS ar
LEFT JOIN
	public.regions AS re
ON
	ar.country_of_origin = re."Country"
	AND ar."Region" = re."Region"
;