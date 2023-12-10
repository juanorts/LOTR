document.addEventListener('DOMContentLoaded', function() {

  function cambiarIdioma(nuevoIdioma) {
    var urlActual = window.location.href;
    var urlNueva = urlActual.replace(/\/(es|en|eus)\//, '/' + nuevoIdioma + '/');
    window.location.href = urlNueva;
  }

  document.getElementById("flag-es").addEventListener("click", function() {
    cambiarIdioma('es');
  });

  document.getElementById("flag-en").addEventListener("click", function() {
    cambiarIdioma('en');
  });

  document.getElementById("flag-eus").addEventListener("click", function() {
    cambiarIdioma('eus');
  });

  var imagen = document.getElementById("anillo-musical");
  var audio = new Audio("/static/audio/lotr.mp3");

  // Evento para reproducir la música
  imagen.addEventListener("click",function() {
      //Al hacer click en la imagen se reproduce la música
      if (audio.paused) {
          audio.play();
      } else {
          audio.pause();
      }

  });

  var imagenesZoom = document.querySelectorAll(".imagenPersonaje");
  var imagenesZoom2 = document.querySelectorAll("imagenPersonaje");

  imagenesZoom2.forEach(function(imagen){
      imagen.addEventListener("mouseover", function(){
          aplicarZoom(imagen);
      });
      imagen.addEventListener('mouseout', function() {
          // Restablece la transformación a su estado original
          this.style.transform = "scale(1)";
        });
  });

  imagenesZoom.forEach(function(imagen){
      imagen.addEventListener("mouseover", function(){
          aplicarZoom(imagen);
      });
      imagen.addEventListener('mouseout', function() {
          // Restablece la transformación a su estado original
          this.style.transform = "scale(1)";
        });
  });

  function aplicarZoom(imagen){
      var tamNuevo = "150%";       
      imagen.style.transform = "scale("+tamNuevo+")";

  }

  //Evento para mover a Gandalf
  var gandalf = document.getElementById("gandalf");
  var bocadillo = document.getElementById("imagen-oculta");

  gandalf.addEventListener("click", function() {
      var start = Date.now(); // timestamp inicial
      var posOriginal = gandalf.style.right;

      var temporizador = setInterval(function() {

          var tiempoPasado = Date.now() - start; // cuánto tiempo ha pasado desde el inicio
          gandalf.style.right = tiempoPasado / 5.4 + 'px'; // movimiento lineal simple

          if (tiempoPasado > 2000){
              clearInterval(temporizador);

              bocadillo.style.display ="inline";   


          } 

          setTimeout(function(){

              bocadillo.style.display ="none"; 

              gandalf.style.right = posOriginal;

          }, 4000);



      }, 20);
  });
});
