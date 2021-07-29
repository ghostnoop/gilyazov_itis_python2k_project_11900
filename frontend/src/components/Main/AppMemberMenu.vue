<template>
  <section class="menu__section" v-bind:class="{'menu__active': activeMenu}">
    <header class="menu__header">
      Учетная запись
      <svg class="symbol__close" v-on:click="closeMenu">
        <use xlink:href="#close"></use>
      </svg>
    </header>
    <div class="menu__user">
      <button class="main__header--username menu__user--avatar">
        ДГ
      </button>
      <div class="menu__user--info">
        <div class="menu__user-name">Дмитрий Герасимов</div>
        <div class="menu__user-email">dmitry.itis.gg@gmail.com</div>
      </div>
    </div>
    <ul class="menu__user--ul">
      <li class="menu__user--li" v-on:click="btnLogout">Выйти</li>
    </ul>
  </section>
</template>

<script>
import router from "@/router";

export default {
  name: "AppMemberMenu",
  data: () => ({}),
  computed: {
    activeMenu() {
      return this.$store.state.activeMenu;
    }
  },
  methods: {
    closeMenu() {
      this.$store.commit('clickMenu')
    },
    btnLogout() {
      this.$store.commit('auth/logout')
      router.push('/login')
    }
  }
}
</script>

<style scoped>

</style>