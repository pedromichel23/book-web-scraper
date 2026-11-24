# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BookscraperPipeline:
    def process_item(self, item):
        adapter = ItemAdapter(item)

        # Strip all whitespaces from strings
        field_names = adapter.field_names()
        for field_name in field_names:
            if field_name != 'description':
                value = adapter.get(field_name)
                #print("############")
                #print(value)
                adapter[field_name] = value[0].strip()

        #Category & Product Type --> switch to lowercase
        lowercase_keys = ['category', 'product_type']
        for lowercase_key in lowercase_keys:
            value = adapter.get(lowercase_key)
            adapter[lowercase_key] = value.lower()

        #Price --> convert to float
        price_keys = ['price', 'price_excl_tax', 'price_incl_tax', 'tax']
        for price_key in price_keys:
            value = adapter.get(price_key)
            #print("############")
            #print(value)
            value = value.replace('£', '')
            #print("############")
            #print(value)
            if value:
                adapter[price_key] = float(value)
            else:
                adapter[price_key] = 0.00

        #Availability --> extrac number of books in stock
        availability_string = adapter.get('availability')
        split_string_array = availability_string.split('(')
        if len(split_string_array) < 2:
            adapter['availability'] = 0
        else:
            availability_array = split_string_array[1].split(' ')
            adapter['availability'] = int(availability_array[0])
        '''
        Otra forma usando regex en lugar de split
        resultado = re.search(r'\((\d+)\s+available\)', texto)
        if resultado:
            cantidad = int(resultado.group(1))
            print(cantidad)
        '''

        #Reviews --> convert string to number
        num_reviews_string = adapter.get('num_reviews')
        adapter['num_reviews'] = int(num_reviews_string)

        #Stars --> convert text to number
        start_string = adapter.get('stars')
        split_stars_array = start_string.split(' ')
        stars_text_value = split_stars_array[1].lower()
        if stars_text_value == 'zero':
            adapter['stars'] = 0
        elif stars_text_value == 'one':
            adapter['stars'] = 1
        elif stars_text_value == 'two':
            adapter['stars'] = 2
        elif stars_text_value == 'three':
            adapter['stars'] = 3
        elif stars_text_value == 'four':
            adapter['stars'] = 4
        elif stars_text_value == 'five':
            adapter['stars'] = 5


        return item
