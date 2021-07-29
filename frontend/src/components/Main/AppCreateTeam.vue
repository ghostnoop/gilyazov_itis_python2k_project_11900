<template>
  <div class="create_team--window" v-bind:class="{'team__window--active':activeModal}">
    <div class="create_team--modal">
      <svg class="symbol__close--modal" v-on:click="closeModal">
        <use xlink:href="#close"></use>
      </svg>
      <div class="team__modal--info">
        <form class="team__modal--form">
          <span class="team__modal--title">Создайте команду</span>
          <span class="team__modal--text">Повысьте производительность: участники команды смогут получать удобный доступ ко всем доскам.</span>
          <div class="modal__group">
            <label for="name_team" class="modal__team--label">Имя команды</label>
            <input type="text" id="name_team" class="modal__team--input" placeholder="Введите название команды"
                   v-model="team.name">
            <div class="modal__team-undertext">Укажите название вашей команды, компании или организации.</div>
          </div>

          <button type="button" class="modal__team--btn" v-on:click="btnTeam">Создать команду</button>
        </form>
      </div>
      <div class="modal__team--background">
        <div class="modal__team--photo">
          <img src="img/empty-board.d1f066971350650d3346.svg" class="modal__team--img" alt="">
          <img src="img/green-face.1a4590e4c12ebbbd161a.svg" alt="" class="modal__team--subimg">
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import store from "../../store"

export default {
  name: "AppCreateTeam",
  data: () => ({
    team: {
      name: '',
      email: ''
    },
    teams: []
  }),
  computed: {
    activeModal() {
      return this.$store.state.activeTeamModal;
    }
  },
  methods: {
    closeModal() {
      this.$store.commit('activeModal')
    },
    fetchTeam() {
      fetch(`http://localhost:9000/api/v1/team/teams?email=${store.getters['auth/user'].email}`, {
        method: "GET",
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${store.getters['auth/token']}`
        },
        mode: "cors"
      }).then(response => response.json())
          .then(result => {
            console.log(result)
            this.teams = result
            console.log(this.teams)
          })
    },
    btnTeam() {
      this.team.email = store.getters['auth/user'].email
      console.log(this.team)
      fetch('http://localhost:9000/api/v1/team/create', {
        method: 'post',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${store.getters['auth/token']}`
        },
        body: JSON.stringify(this.team),
        mode: "cors"
      }).then(response => response.json())
          .then(result => {
            if (result.status === 200) {
              this.$store.commit('activeModal')
              this.$store.dispatch('main/mountTeams')
            }
          })

    }
  },
  mounted() {
  }
}
</script>

<style scoped>

</style>