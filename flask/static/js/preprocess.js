export function simplifyArray(imageArr) {
    var simpleArr = imageArr.filter(
        (value, index) => (index + 1) % 4 == 0);
     simpleArr = simpleArr.map(
         value => {
             if(value > 150){
                 return 1;
             }else{
                 return 0;
             }
         });
    return Array.from(simpleArr)
}