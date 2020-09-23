$(function(){
    window.setInterval(function(){
        $.ajax({
            url: '/canbus',
            contentType: 'application/json',
            success: function(response){
                
                console.log(response['steering']);
                document.getElementById("time").innerHTML=response['time'];
                document.getElementById("speed").innerHTML=response['speed'];
                var steer = response['steering']
                document.getElementById("P").classList.remove('active');
                document.getElementById("R").classList.remove('active');
                document.getElementById("N").classList.remove('active');
                document.getElementById("D").classList.remove('active');
                if(response['gear'] == "P"){
                    document.getElementById("P").classList.add('active');
                }
                else if(response['gear'] == "R"){
                    document.getElementById("R").classList.add('active');
                }
                else if(response['gear'] == "N"){
                    document.getElementById("N").classList.add('active');
                }
                else if(response['gear'] == "D"){
                    document.getElementById("D").classList.add('active');
                }
                document.getElementById('steering').style['transform']='rotate('+steer+'deg)'
                    
            }
        });
      }, 10);
});