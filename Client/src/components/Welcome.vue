<template>
  <div class="welcome container">
    <div class='welcome-header'>
      <h3>Welcome to Finance Hero</h3>
      <h4>Find your recommended portfolio today!</h4>
    </div>

    <div id = "form">
      <div class='age-container'>
        <h3>My age is </h3>
        <b-form-select name="age" size="sm" id="age" class='age'>
          <option>18-25</option>
          <option>25-35</option>
          <option>35-65</option>
        </b-form-select>
      </div>
      <div class='risk-app-container'>
        <h3>My risk appeitie is </h3>
        <b-form-select name="risk-app" id="risk-app" size="sm" class='risk-app'>
          <option value="low">Low</option>
          <option value="moderate">Moderate</option>
          <option value="high">High</option>
        </b-form-select>
      </div>
      <div class='capital-container'>
        <h3>My estimated investment capital </h3>
        <b-form-select name="capital" id="capital" size="sm" class='capital'>
          <option value="low">Less than $5000</option>
          <option value="moderate">Between $5000 to $10,000</option>
          <option value="high">Above $10,000</option>
        </b-form-select>
      </div>
      
      <br>
      <router-link to='/portfolio'>
        <b-button onClick= "#portflio"> Get my portfolio! </b-button>
      </router-link>
    </div>

  </div>
</template>

<script>

export default {
  name: 'Welcome',
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.welcome{
  margin-top: 100px;
}

.welcome-header{
  padding-top: 10px;
  margin-bottom: 20px;
}

h3 {
  margin: 40px 0 0;
  display: inline !important;

}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}

.age, .risk-app, .capital{
  width: 200px;
}

.age-container, .risk-app-container, .capital-container{
  padding-bottom: 20px;
}

</style>
