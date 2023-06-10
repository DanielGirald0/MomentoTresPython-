let boton=document.getElementById("btnreporte")
boton.addEventListener("click",function(evento){
    evento.preventDefault()
    let contenedor=document.getElementById("contenedor")
    contenedor.classList.remove("d-none")

    let nombreUsuario=document.getElementById("nombre").value
    let mensaje=document.getElementById("mensaje")

    mensaje.textContent=`Apreciado usuario: ${nombreUsuario}, hemos generado su reporte: `
   

})