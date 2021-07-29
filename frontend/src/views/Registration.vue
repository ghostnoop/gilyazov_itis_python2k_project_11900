<template>
  <app-sprite></app-sprite>
  <section class="login__section">
    <header class="login__header">
      <div class="logo__login">
        <h2 class="logo__header__text">Iremember</h2>
      </div>
    </header>
    <div class="login__content">
      <app-registration></app-registration>
    </div>
    <div class="login__background">
    </div>
  </section>
</template>

<script>
import AppSprite from "@/sprite/AppSprite";
import AppRegistration from "@/components/Registration/AppRegistration";

export default {
  name: "Registration",
  components: {AppSprite, AppRegistration}
}
</script>

<style scoped>

</style>
