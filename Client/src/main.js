import Vue from 'vue'
import Home from './components/Home.vue'
import Baidu from './components/Baidu.vue'
import Welcome from './components/Welcome.vue'
import PieChart from './components/PieChart.vue'
import Transcript from './components/Transcript.vue'
import App from './App.vue'
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import VueRouter from 'vue-router'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VueRouter)

const router = new VueRouter({
  routes: [
    { path: '/', component: Welcome},
    { path: '/portfolio', component: PieChart},
    { path: '/stocks', component: Home},
    { path: '/baidu', component: Baidu},
    { path: '/transcript', component: Transcript} 
  ]
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
