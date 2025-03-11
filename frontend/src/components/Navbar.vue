<template>
     
          
            
        <div class="d-flex justify-content-center mt-1 mb-1 bg-gray-100 p-10">
            <div class="bg-white p-6 rounded-lg shadow-md">
                <h1 class="text-2xl font-bold text-blue-500">Employee Management Portal</h1>
            </div>
        </div>
   
        <nav class="navbar navbar-expand-md navbar-light bg-ligh">
            <ul class="navbar-nav center">
                <li class="nav-item m-1">
                    <router-link class="btn btn-light btn-outline-primary"
                    to="/home">Home</router-link>
                </li>
                <li class="nav-item m-1">
                    <router-link class="btn btn-light btn-outline-primary"
                    to="/department">Department</router-link>
                </li>
                <li class="nav-item m-1">
                    <router-link class="btn btn-light btn-outline-primary"
                    to="/employee">Employee</router-link>
                </li>
            </ul>
        </nav>
</template>

<script>
    export default {
        /* eslint-disable */
        name: "Navbar",
    }
</script>
