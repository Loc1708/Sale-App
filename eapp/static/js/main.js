function addToCart(id,name,price){
    fetch('/api/carts', {
        method: 'post',
        body: JSON.stringify({
            'id':id
                'name': name,
                'price': price

        }),
        headers: {
            'Content-Type': 'application/json'
        }
    }).then(data => data.json()).then(data =>{
        console.info(data)
    })
}