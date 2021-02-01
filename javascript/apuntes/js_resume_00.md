## Implementaciones de Javascript (ES6 - EcmaScript2015)

**recursividad**: consiste en funciones que se llaman a sí mismas, evitando el uso de bucles y otros iteradores

```javascript

function factorial(n) {

    if (n<=1) return 1;
    
    return n* factorial(n-1);
}

```

```javascript

function sum(arr, n) {

    if (n<=0) {
        return 0;
    } else {
        return sum(arr, n-1) + arr[n-1];
    }
}

```

- [explicación complementaria 1](https://www.campusmvp.es/recursos/post/Que-es-la-recursividad-o-recursion-Un-ejemplo-con-JavaScript.aspx)