function openCity(evt, cityName) {
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none"; // Hide all tab contents
            }
            tablinks = document.querySelectorAll(".dashbordlinks a");
            tablinks.forEach(link => link.classList.remove("active")); // Remove active class
            document.getElementById(cityName).style.display = "block"; // Show the clicked tab
            evt.currentTarget.classList.add("active"); // Add active class to the clicked button
        }

        // Open the default tab on page load
        document.getElementById("defaultOpen").click();

        var modal = document.getElementById('id01');

