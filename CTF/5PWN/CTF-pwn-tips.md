





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">

  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/frameworks-521cbf980c80.css" integrity="sha512-Uhy/mAyAx1HfsenmjQ85ASpOk5bjt2Ay03pNeixXIvkHlEm5S+N4u0HWfDGhvsGYx4bGyviXWGGPZeIffqYcNA==" media="all" rel="stylesheet" />
  <link crossorigin="anonymous" href="https://assets-cdn.github.com/assets/github-bab09cdfa5e9.css" integrity="sha512-urCc36XpOB6NJpSUfwUO4198a84yfDnoKASZ+D+7pCjpTpQ3YrhkgX9SgIpI83PiKF87mXoMJHJ/nE0eXNeTqA==" media="all" rel="stylesheet" />
  
  
  
  

  <meta name="viewport" content="width=device-width">
  
  <title>CTF-pwn-tips/README.md at master · Naetw/CTF-pwn-tips</title>
  <link rel="search" type="application/opensearchdescription+xml" href="/opensearch.xml" title="GitHub">
  <link rel="fluid-icon" href="https://github.com/fluidicon.png" title="GitHub">
  <meta property="fb:app_id" content="1401488693436528">

    
    <meta content="https://avatars1.githubusercontent.com/u/21299767?s=400&amp;v=4" property="og:image" /><meta content="GitHub" property="og:site_name" /><meta content="object" property="og:type" /><meta content="Naetw/CTF-pwn-tips" property="og:title" /><meta content="https://github.com/Naetw/CTF-pwn-tips" property="og:url" /><meta content="CTF-pwn-tips - Here records some tips about pwn." property="og:description" />

  <link rel="assets" href="https://assets-cdn.github.com/">
  <link rel="web-socket" href="wss://live.github.com/_sockets/VjI6MjQ0OTcwMjU4OjZkNmIzMzZmMzJmMjNhMjBlZmQ0M2E0YzQxZGRhYzU0ZDc2MzBlZmE1YmMzODlmNTUyYjM5OWEzZGFlNTgyMzY=--960862e2f3f0fdda88aaecb86cd8db62577c375f">
  <meta name="pjax-timeout" content="1000">
  <link rel="sudo-modal" href="/sessions/sudo_modal">
  <meta name="request-id" content="E234:11A90:91841A0:D23FC56:5A74094B" data-pjax-transient>
  

  <meta name="selected-link" value="repo_source" data-pjax-transient>

    <meta name="google-site-verification" content="KT5gs8h0wvaagLKAVWq8bbeNwnZZK1r1XQysX3xurLU">
  <meta name="google-site-verification" content="ZzhVyEFwb7w3e0-uOTltm8Jsck2F5StVihD0exw2fsA">
  <meta name="google-site-verification" content="GXs5KoUUkNCoaAZn7wPN-t01Pywp9M3sEjnt_3_ZWPc">
    <meta name="google-analytics" content="UA-3769691-2">

<meta content="collector.githubapp.com" name="octolytics-host" /><meta content="github" name="octolytics-app-id" /><meta content="https://collector.githubapp.com/github-external/browser_event" name="octolytics-event-url" /><meta content="E234:11A90:91841A0:D23FC56:5A74094B" name="octolytics-dimension-request_id" /><meta content="sea" name="octolytics-dimension-region_edge" /><meta content="iad" name="octolytics-dimension-region_render" /><meta content="18084255" name="octolytics-actor-id" /><meta content="yanlijian2012" name="octolytics-actor-login" /><meta content="039917e2a8f5ba9393a5b72bc1d67f6401c6dddb78f420196ffcff9aad78c254" name="octolytics-actor-hash" />
<meta content="https://github.com/hydro_browser_events" name="hydro-events-url" />
<meta content="/&lt;user-name&gt;/&lt;repo-name&gt;/blob/show" data-pjax-transient="true" name="analytics-location" />




  <meta class="js-ga-set" name="dimension1" content="Logged In">


  

      <meta name="hostname" content="github.com">
  <meta name="user-login" content="yanlijian2012">

      <meta name="expected-hostname" content="github.com">
    <meta name="js-proxy-site-detection-payload" content="M2E0ZTFkMDg0ODMzZjA2NDA4OThlZjkwY2VjMDNkM2I1MWY1OWU0NDBiMGI1NTI2NWE5Y2M0YTVhMWZlZGVjYnx7InJlbW90ZV9hZGRyZXNzIjoiNjYuMTEyLjIyMS4xMzgiLCJyZXF1ZXN0X2lkIjoiRTIzNDoxMUE5MDo5MTg0MUEwOkQyM0ZDNTY6NUE3NDA5NEIiLCJ0aW1lc3RhbXAiOjE1MTc1NTQwMzAsImhvc3QiOiJnaXRodWIuY29tIn0=">

    <meta name="enabled-features" content="UNIVERSE_BANNER,MULTIPLE_ATTRIBUTION,FREE_TRIALS,MARKETPLACE_HERO_CARD_UPLOADER,CONTRIBUTOR_FLAGGED_CONTENT">

  <meta name="html-safe-nonce" content="4e46fb05486ab8180de0377ed9ea6da8cf587248">

  <meta http-equiv="x-pjax-version" content="5907440b09adafe0c1fa8d5253427e96">
  

      <link href="https://github.com/Naetw/CTF-pwn-tips/commits/master.atom" rel="alternate" title="Recent Commits to CTF-pwn-tips:master" type="application/atom+xml">

  <meta name="description" content="CTF-pwn-tips - Here records some tips about pwn.">
  <meta name="go-import" content="github.com/Naetw/CTF-pwn-tips git https://github.com/Naetw/CTF-pwn-tips.git">

  <meta content="21299767" name="octolytics-dimension-user_id" /><meta content="Naetw" name="octolytics-dimension-user_login" /><meta content="79437230" name="octolytics-dimension-repository_id" /><meta content="Naetw/CTF-pwn-tips" name="octolytics-dimension-repository_nwo" /><meta content="true" name="octolytics-dimension-repository_public" /><meta content="false" name="octolytics-dimension-repository_is_fork" /><meta content="79437230" name="octolytics-dimension-repository_network_root_id" /><meta content="Naetw/CTF-pwn-tips" name="octolytics-dimension-repository_network_root_nwo" /><meta content="false" name="octolytics-dimension-repository_explore_github_marketplace_ci_cta_shown" />


    <link rel="canonical" href="https://github.com/Naetw/CTF-pwn-tips/blob/master/README.md" data-pjax-transient>


  <meta name="browser-stats-url" content="https://api.github.com/_private/browser/stats">

  <meta name="browser-errors-url" content="https://api.github.com/_private/browser/errors">

  <link rel="mask-icon" href="https://assets-cdn.github.com/pinned-octocat.svg" color="#000000">
  <link rel="icon" type="image/x-icon" class="js-site-favicon" href="https://assets-cdn.github.com/favicon.ico">

<meta name="theme-color" content="#1e2327">



  </head>

  <body class="logged-in env-production page-blob">
    

  <div class="position-relative js-header-wrapper ">
    <a href="#start-of-content" tabindex="1" class="bg-black text-white p-3 show-on-focus js-skip-to-content">Skip to content</a>
    <div id="js-pjax-loader-bar" class="pjax-loader-bar"><div class="progress"></div></div>

    
    
    



        
<header class="Header  f5" role="banner">
  <div class="d-flex px-3 flex-justify-between container-lg">
    <div class="d-flex flex-justify-between">
      <a class="header-logo-invertocat" href="https://github.com/" data-hotkey="g d" aria-label="Homepage" data-ga-click="Header, go to dashboard, icon:logo">
  <svg aria-hidden="true" class="octicon octicon-mark-github" height="32" version="1.1" viewBox="0 0 16 16" width="32"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>


    </div>

    <div class="HeaderMenu d-flex flex-justify-between flex-auto">
      <div class="d-flex">
            <div class="">
              <div class="header-search scoped-search site-scoped-search js-site-search" role="search">
  <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Naetw/CTF-pwn-tips/search" class="js-site-search-form" data-scoped-search-url="/Naetw/CTF-pwn-tips/search" data-unscoped-search-url="/search" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
    <label class="form-control header-search-wrapper js-chromeless-input-container">
        <a href="/Naetw/CTF-pwn-tips/blob/master/README.md" class="header-search-scope no-underline">This repository</a>
      <input type="text"
        class="form-control header-search-input js-site-search-focus js-site-search-field is-clearable"
        data-hotkey="s"
        name="q"
        value=""
        placeholder="Search"
        aria-label="Search this repository"
        data-unscoped-placeholder="Search GitHub"
        data-scoped-placeholder="Search"
        autocapitalize="off">
        <input type="hidden" class="js-site-search-type-field" name="type" >
    </label>
</form></div>

            </div>

          <ul class="d-flex pl-2 flex-items-center text-bold list-style-none" role="navigation">
            <li>
              <a href="/pulls" aria-label="Pull requests you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:pulls context:user" data-hotkey="g p" data-selected-links="/pulls /pulls/assigned /pulls/mentioned /pulls">
                Pull requests
</a>            </li>
            <li>
              <a href="/issues" aria-label="Issues you created" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:issues context:user" data-hotkey="g i" data-selected-links="/issues /issues/assigned /issues/mentioned /issues">
                Issues
</a>            </li>
                <li>
                  <a href="/marketplace" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:marketplace context:user" data-selected-links=" /marketplace">
                    Marketplace
</a>                </li>
            <li>
              <a href="/explore" class="js-selected-navigation-item HeaderNavlink px-2" data-ga-click="Header, click, Nav menu - item:explore" data-selected-links="/explore /trending /trending/developers /integrations /integrations/feature/code /integrations/feature/collaborate /integrations/feature/ship showcases showcases_search showcases_landing /explore">
                Explore
</a>            </li>
          </ul>
      </div>

      <div class="d-flex">
        
<ul class="user-nav d-flex flex-items-center list-style-none" id="user-links">
  <li class="dropdown js-menu-container">
    <span class="d-inline-block  px-2">
      

    </span>
  </li>

  <li class="dropdown js-menu-container">
    <details class="dropdown-details details-reset js-dropdown-details d-flex px-2 flex-items-center">
      <summary class="HeaderNavlink"
         aria-label="Create new…"
         data-ga-click="Header, create new, icon:add">
        <svg aria-hidden="true" class="octicon octicon-plus float-left mr-1 mt-1" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 9H7v5H5V9H0V7h5V2h2v5h5z"/></svg>
        <span class="dropdown-caret mt-1"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        
<a class="dropdown-item" href="/new" data-ga-click="Header, create new repository">
  New repository
</a>

  <a class="dropdown-item" href="/new/import" data-ga-click="Header, import a repository">
    Import repository
  </a>

<a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, create new gist">
  New gist
</a>

  <a class="dropdown-item" href="/organizations/new" data-ga-click="Header, create new organization">
    New organization
  </a>



  <div class="dropdown-divider"></div>
  <div class="dropdown-header">
    <span title="Naetw/CTF-pwn-tips">This repository</span>
  </div>
    <a class="dropdown-item" href="/Naetw/CTF-pwn-tips/issues/new" data-ga-click="Header, create new issue">
      New issue
    </a>

      </ul>
    </details>
  </li>

  <li class="dropdown js-menu-container">

    <details class="dropdown-details details-reset js-dropdown-details d-flex pl-2 flex-items-center">
      <summary class="HeaderNavlink name mt-1"
        aria-label="View profile and more"
        data-ga-click="Header, show menu, icon:avatar">
        <img alt="@yanlijian2012" class="avatar float-left mr-1" src="https://avatars0.githubusercontent.com/u/18084255?s=40&amp;v=4" height="20" width="20">
        <span class="dropdown-caret"></span>
      </summary>

      <ul class="dropdown-menu dropdown-menu-sw">
        <li class="dropdown-header header-nav-current-user css-truncate">
          Signed in as <strong class="css-truncate-target">yanlijian2012</strong>
        </li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="/yanlijian2012" data-ga-click="Header, go to profile, text:your profile">
          Your profile
        </a></li>
        <li><a class="dropdown-item" href="/yanlijian2012?tab=stars" data-ga-click="Header, go to starred repos, text:your stars">
          Your stars
        </a></li>
          <li><a class="dropdown-item" href="https://gist.github.com/" data-ga-click="Header, your gists, text:your gists">Your Gists</a></li>

        <li class="dropdown-divider"></li>

        <li><a class="dropdown-item" href="https://help.github.com" data-ga-click="Header, go to help, text:help">
          Help
        </a></li>

        <li><a class="dropdown-item" href="/settings/profile" data-ga-click="Header, go to settings, icon:settings">
          Settings
        </a></li>

        <li><!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="logout-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="msI1h7cr91ZXreVZFCRiUkkHicmY+V4Gl/sjAeojeZ60xZTvLshqzWm8KQQXh1R561XQwfXg5MGhTpr31DX9UQ==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
        </form></li>
      </ul>
    </details>
  </li>
</ul>


        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/logout" class="sr-only right-0" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="g3UqJl4K+y1CnfEer2mKo47DhxMGrpbwu/Dp8XZiLg+tcotOx+lmtnyMPUOsyryILJHeG2u3LDeNRVAHSHSqwA==" /></div>
          <button type="submit" class="dropdown-item dropdown-signout" data-ga-click="Header, sign out, icon:logout">
            Sign out
          </button>
</form>      </div>
    </div>
  </div>
</header>

      

  </div>

  <div id="start-of-content" class="show-on-focus"></div>

    <div id="js-flash-container">
</div>



  <div role="main" class="application-main ">
        <div itemscope itemtype="http://schema.org/SoftwareSourceCode" class="">
    <div id="js-repo-pjax-container" data-pjax-container >
      






  <div class="pagehead repohead instapaper_ignore readability-menu experiment-repo-nav  ">
    <div class="repohead-details-container clearfix container">

      <ul class="pagehead-actions">
  <li>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/notifications/subscribe" class="js-social-container" data-autosubmit="true" data-remote="true" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="LoMoFF8F8NZKjyB15IxUwX9On8xb1jr/sDVM5laPo38fvQUvM/HdzSdruqxteimGwKr5DSwpDyN8vMdNVweM+Q==" /></div>      <input class="form-control" id="repository_id" name="repository_id" type="hidden" value="79437230" />

        <div class="select-menu js-menu-container js-select-menu">
          <a href="/Naetw/CTF-pwn-tips/subscription"
            class="btn btn-sm btn-with-count select-menu-button js-menu-target"
            role="button"
            aria-haspopup="true"
            aria-expanded="false"
            aria-label="Toggle repository notifications menu"
            data-ga-click="Repository, click Watch settings, action:blob#show">
            <span class="js-select-button">
                <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                Watch
            </span>
          </a>
          <a class="social-count js-social-count"
            href="/Naetw/CTF-pwn-tips/watchers"
            aria-label="15 users are watching this repository">
            15
          </a>

        <div class="select-menu-modal-holder">
          <div class="select-menu-modal subscription-menu-modal js-menu-content">
            <div class="select-menu-header js-navigation-enable" tabindex="-1">
              <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
              <span class="select-menu-title">Notifications</span>
            </div>

              <div class="select-menu-list js-navigation-container" role="menu">

                <div class="select-menu-item js-navigation-item selected" role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input checked="checked" id="do_included" name="do" type="radio" value="included" />
                    <span class="select-menu-item-heading">Not watching</span>
                    <span class="description">Be notified when participating or @mentioned.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                      Watch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_subscribed" name="do" type="radio" value="subscribed" />
                    <span class="select-menu-item-heading">Watching</span>
                    <span class="description">Be notified of all conversations.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-eye" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.06 2C3 2 0 8 0 8s3 6 8.06 6C13 14 16 8 16 8s-3-6-7.94-6zM8 12c-2.2 0-4-1.78-4-4 0-2.2 1.8-4 4-4 2.22 0 4 1.8 4 4 0 2.22-1.78 4-4 4zm2-4c0 1.11-.89 2-2 2-1.11 0-2-.89-2-2 0-1.11.89-2 2-2 1.11 0 2 .89 2 2z"/></svg>
                        Unwatch
                    </span>
                  </div>
                </div>

                <div class="select-menu-item js-navigation-item " role="menuitem" tabindex="0">
                  <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
                  <div class="select-menu-item-text">
                    <input id="do_ignore" name="do" type="radio" value="ignore" />
                    <span class="select-menu-item-heading">Ignoring</span>
                    <span class="description">Never be notified.</span>
                    <span class="js-select-button-text hidden-select-button-text">
                      <svg aria-hidden="true" class="octicon octicon-mute" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8 2.81v10.38c0 .67-.81 1-1.28.53L3 10H1c-.55 0-1-.45-1-1V7c0-.55.45-1 1-1h2l3.72-3.72C7.19 1.81 8 2.14 8 2.81zm7.53 3.22l-1.06-1.06-1.97 1.97-1.97-1.97-1.06 1.06L11.44 8 9.47 9.97l1.06 1.06 1.97-1.97 1.97 1.97 1.06-1.06L13.56 8l1.97-1.97z"/></svg>
                        Stop ignoring
                    </span>
                  </div>
                </div>

              </div>

            </div>
          </div>
        </div>
</form>
  </li>

  <li>
    
  <div class="js-toggler-container js-social-container starring-container ">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Naetw/CTF-pwn-tips/unstar" class="starred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="EGD0SHqZWTsBmhTcvMajynSRbfw29NZq2U1fMbmCuMZJoFV43l3sCNsngBMc70YIHSGmUb89ynnJgu7a05ZKXQ==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Unstar this repository" title="Unstar Naetw/CTF-pwn-tips"
        data-ga-click="Repository, click unstar button, action:blob#show; text:Unstar">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Unstar
      </button>
        <a class="social-count js-social-count" href="/Naetw/CTF-pwn-tips/stargazers"
           aria-label="364 users starred this repository">
          364
        </a>
</form>
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Naetw/CTF-pwn-tips/star" class="unstarred js-social-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="zFgNufoQX+dBRjgRypVN7t9yxc4qr+q39sjHAl7I9wyFM6DfufL7ZohN/FfobO9Pv5K5rkh5rIgF2NQHSVPMxg==" /></div>
      <input type="hidden" name="context" value="repository"></input>
      <button
        type="submit"
        class="btn btn-sm btn-with-count js-toggler-target"
        aria-label="Star this repository" title="Star Naetw/CTF-pwn-tips"
        data-ga-click="Repository, click star button, action:blob#show; text:Star">
        <svg aria-hidden="true" class="octicon octicon-star" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M14 6l-4.9-.64L7 1 4.9 5.36 0 6l3.6 3.26L2.67 14 7 11.67 11.33 14l-.93-4.74z"/></svg>
        Star
      </button>
        <a class="social-count js-social-count" href="/Naetw/CTF-pwn-tips/stargazers"
           aria-label="364 users starred this repository">
          364
        </a>
</form>  </div>

  </li>

  <li>
          <a href="#fork-destination-box" class="btn btn-sm btn-with-count"
              title="Fork your own copy of Naetw/CTF-pwn-tips to your account"
              aria-label="Fork your own copy of Naetw/CTF-pwn-tips to your account"
              rel="facebox"
              data-ga-click="Repository, show fork modal, action:blob#show; text:Fork">
              <svg aria-hidden="true" class="octicon octicon-repo-forked" height="16" version="1.1" viewBox="0 0 10 16" width="10"><path fill-rule="evenodd" d="M8 1a1.993 1.993 0 0 0-1 3.72V6L5 8 3 6V4.72A1.993 1.993 0 0 0 2 1a1.993 1.993 0 0 0-1 3.72V6.5l3 3v1.78A1.993 1.993 0 0 0 5 15a1.993 1.993 0 0 0 1-3.72V9.5l3-3V4.72A1.993 1.993 0 0 0 8 1zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3 10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zm3-10c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
            Fork
          </a>

          <div id="fork-destination-box" style="display: none;">
            <h2 class="facebox-header" data-facebox-id="facebox-header">Where should we fork this repository?</h2>
            <include-fragment src=""
                class="js-fork-select-fragment fork-select-fragment"
                data-url="/Naetw/CTF-pwn-tips/fork?fragment=1">
              <img alt="Loading" height="64" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-128.gif" width="64" />
            </include-fragment>
          </div>

    <a href="/Naetw/CTF-pwn-tips/network" class="social-count"
       aria-label="47 users forked this repository">
      47
    </a>
  </li>
</ul>

      <h1 class="public ">
  <svg aria-hidden="true" class="octicon octicon-repo" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M4 9H3V8h1v1zm0-3H3v1h1V6zm0-2H3v1h1V4zm0-2H3v1h1V2zm8-1v12c0 .55-.45 1-1 1H6v2l-1.5-1.5L3 16v-2H1c-.55 0-1-.45-1-1V1c0-.55.45-1 1-1h10c.55 0 1 .45 1 1zm-1 10H1v2h2v-1h3v1h5v-2zm0-10H2v9h9V1z"/></svg>
  <span class="author" itemprop="author"><a href="/Naetw" class="url fn" rel="author">Naetw</a></span><!--
--><span class="path-divider">/</span><!--
--><strong itemprop="name"><a href="/Naetw/CTF-pwn-tips" data-pjax="#js-repo-pjax-container">CTF-pwn-tips</a></strong>

</h1>

    </div>
    
<nav class="reponav js-repo-nav js-sidenav-container-pjax container"
     itemscope
     itemtype="http://schema.org/BreadcrumbList"
     role="navigation"
     data-pjax="#js-repo-pjax-container">

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/Naetw/CTF-pwn-tips" class="js-selected-navigation-item selected reponav-item" data-hotkey="g c" data-selected-links="repo_source repo_downloads repo_commits repo_releases repo_tags repo_branches repo_packages /Naetw/CTF-pwn-tips" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-code" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M9.5 3L8 4.5 11.5 8 8 11.5 9.5 13 14 8 9.5 3zm-5 0L0 8l4.5 5L6 11.5 2.5 8 6 4.5 4.5 3z"/></svg>
      <span itemprop="name">Code</span>
      <meta itemprop="position" content="1">
</a>  </span>

    <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
      <a href="/Naetw/CTF-pwn-tips/issues" class="js-selected-navigation-item reponav-item" data-hotkey="g i" data-selected-links="repo_issues repo_labels repo_milestones /Naetw/CTF-pwn-tips/issues" itemprop="url">
        <svg aria-hidden="true" class="octicon octicon-issue-opened" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M7 2.3c3.14 0 5.7 2.56 5.7 5.7s-2.56 5.7-5.7 5.7A5.71 5.71 0 0 1 1.3 8c0-3.14 2.56-5.7 5.7-5.7zM7 1C3.14 1 0 4.14 0 8s3.14 7 7 7 7-3.14 7-7-3.14-7-7-7zm1 3H6v5h2V4zm0 6H6v2h2v-2z"/></svg>
        <span itemprop="name">Issues</span>
        <span class="Counter">0</span>
        <meta itemprop="position" content="2">
</a>    </span>

  <span itemscope itemtype="http://schema.org/ListItem" itemprop="itemListElement">
    <a href="/Naetw/CTF-pwn-tips/pulls" class="js-selected-navigation-item reponav-item" data-hotkey="g p" data-selected-links="repo_pulls /Naetw/CTF-pwn-tips/pulls" itemprop="url">
      <svg aria-hidden="true" class="octicon octicon-git-pull-request" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 11.28V5c-.03-.78-.34-1.47-.94-2.06C9.46 2.35 8.78 2.03 8 2H7V0L4 3l3 3V4h1c.27.02.48.11.69.31.21.2.3.42.31.69v6.28A1.993 1.993 0 0 0 10 15a1.993 1.993 0 0 0 1-3.72zm-1 2.92c-.66 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2zM4 3c0-1.11-.89-2-2-2a1.993 1.993 0 0 0-1 3.72v6.56A1.993 1.993 0 0 0 2 15a1.993 1.993 0 0 0 1-3.72V4.72c.59-.34 1-.98 1-1.72zm-.8 10c0 .66-.55 1.2-1.2 1.2-.65 0-1.2-.55-1.2-1.2 0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2zM2 4.2C1.34 4.2.8 3.65.8 3c0-.65.55-1.2 1.2-1.2.65 0 1.2.55 1.2 1.2 0 .65-.55 1.2-1.2 1.2z"/></svg>
      <span itemprop="name">Pull requests</span>
      <span class="Counter">0</span>
      <meta itemprop="position" content="3">
</a>  </span>

    <a href="/Naetw/CTF-pwn-tips/projects" class="js-selected-navigation-item reponav-item" data-hotkey="g b" data-selected-links="repo_projects new_repo_project repo_project /Naetw/CTF-pwn-tips/projects">
      <svg aria-hidden="true" class="octicon octicon-project" height="16" version="1.1" viewBox="0 0 15 16" width="15"><path fill-rule="evenodd" d="M10 12h3V2h-3v10zm-4-2h3V2H6v8zm-4 4h3V2H2v12zm-1 1h13V1H1v14zM14 0H1a1 1 0 0 0-1 1v14a1 1 0 0 0 1 1h13a1 1 0 0 0 1-1V1a1 1 0 0 0-1-1z"/></svg>
      Projects
      <span class="Counter" >0</span>
</a>
    <a href="/Naetw/CTF-pwn-tips/wiki" class="js-selected-navigation-item reponav-item" data-hotkey="g w" data-selected-links="repo_wiki /Naetw/CTF-pwn-tips/wiki">
      <svg aria-hidden="true" class="octicon octicon-book" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M3 5h4v1H3V5zm0 3h4V7H3v1zm0 2h4V9H3v1zm11-5h-4v1h4V5zm0 2h-4v1h4V7zm0 2h-4v1h4V9zm2-6v9c0 .55-.45 1-1 1H9.5l-1 1-1-1H2c-.55 0-1-.45-1-1V3c0-.55.45-1 1-1h5.5l1 1 1-1H15c.55 0 1 .45 1 1zm-8 .5L7.5 3H2v9h6V3.5zm7-.5H9.5l-.5.5V12h6V3z"/></svg>
      Wiki
</a>

  <a href="/Naetw/CTF-pwn-tips/pulse" class="js-selected-navigation-item reponav-item" data-selected-links="repo_graphs repo_contributors dependency_graph pulse /Naetw/CTF-pwn-tips/pulse">
    <svg aria-hidden="true" class="octicon octicon-graph" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M16 14v1H0V0h1v14h15zM5 13H3V8h2v5zm4 0H7V3h2v10zm4 0h-2V6h2v7z"/></svg>
    Insights
</a>

</nav>


  </div>

<div class="container new-discussion-timeline experiment-repo-nav  ">
  <div class="repository-content ">

    
  <a href="/Naetw/CTF-pwn-tips/blob/dbd93c9258328cc9f5ba670dfd3fa07c042ea811/README.md" class="d-none js-permalink-shortcut" data-hotkey="y">Permalink</a>

  <!-- blob contrib key: blob_contributors:v21:18d610e08d17a648dca01a99ac629746 -->

  <div class="file-navigation js-zeroclipboard-container">
    
<div class="select-menu branch-select-menu js-menu-container js-select-menu float-left">
  <button class=" btn btn-sm select-menu-button js-menu-target css-truncate" data-hotkey="w"
    
    type="button" aria-label="Switch branches or tags" aria-expanded="false" aria-haspopup="true">
      <i>Branch:</i>
      <span class="js-select-button css-truncate-target">master</span>
  </button>

  <div class="select-menu-modal-holder js-menu-content js-navigation-container" data-pjax>

    <div class="select-menu-modal">
      <div class="select-menu-header">
        <svg aria-label="Close" class="octicon octicon-x js-menu-close" height="16" role="img" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
        <span class="select-menu-title">Switch branches/tags</span>
      </div>

      <div class="select-menu-filters">
        <div class="select-menu-text-filter">
          <input type="text" aria-label="Filter branches/tags" id="context-commitish-filter-field" class="form-control js-filterable-field js-navigation-enable" placeholder="Filter branches/tags">
        </div>
        <div class="select-menu-tabs">
          <ul>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="branches" data-filter-placeholder="Filter branches/tags" class="js-select-menu-tab" role="tab">Branches</a>
            </li>
            <li class="select-menu-tab">
              <a href="#" data-tab-filter="tags" data-filter-placeholder="Find a tag…" class="js-select-menu-tab" role="tab">Tags</a>
            </li>
          </ul>
        </div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="branches" role="menu">

        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


            <a class="select-menu-item js-navigation-item js-navigation-open selected"
               href="/Naetw/CTF-pwn-tips/blob/master/README.md"
               data-name="master"
               data-skip-pjax="true"
               rel="nofollow">
              <svg aria-hidden="true" class="octicon octicon-check select-menu-item-icon" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M12 5l-8 8-4-4 1.5-1.5L4 10l6.5-6.5z"/></svg>
              <span class="select-menu-item-text css-truncate-target js-select-menu-filter-text">
                master
              </span>
            </a>
        </div>

          <div class="select-menu-no-results">Nothing to show</div>
      </div>

      <div class="select-menu-list select-menu-tab-bucket js-select-menu-tab-bucket" data-tab-filter="tags">
        <div data-filterable-for="context-commitish-filter-field" data-filterable-type="substring">


        </div>

        <div class="select-menu-no-results">Nothing to show</div>
      </div>

    </div>
  </div>
</div>

    <div class="BtnGroup float-right">
      <a href="/Naetw/CTF-pwn-tips/find/master"
            class="js-pjax-capture-input btn btn-sm BtnGroup-item"
            data-pjax
            data-hotkey="t">
        Find file
      </a>
      <button aria-label="Copy file path to clipboard" class="js-zeroclipboard btn btn-sm BtnGroup-item tooltipped tooltipped-s" data-copied-hint="Copied!" type="button">Copy path</button>
    </div>
    <div class="breadcrumb js-zeroclipboard-target">
      <span class="repo-root js-repo-root"><span class="js-path-segment"><a href="/Naetw/CTF-pwn-tips" data-pjax="true"><span>CTF-pwn-tips</span></a></span></span><span class="separator">/</span><strong class="final-path">README.md</strong>
    </div>
  </div>


  <include-fragment class="commit-tease" src="/Naetw/CTF-pwn-tips/contributors/master/README.md">
    <div>
      Fetching contributors&hellip;
    </div>

    <div class="commit-tease-contributors">
      <img alt="" class="loader-loading float-left" height="16" src="https://assets-cdn.github.com/images/spinners/octocat-spinner-32-EAF2F5.gif" width="16" />
      <span class="loader-error">Cannot retrieve contributors at this time</span>
    </div>
</include-fragment>

  <div class="file">
    <div class="file-header">
  <div class="file-actions">

    <div class="BtnGroup">
      <a href="/Naetw/CTF-pwn-tips/raw/master/README.md" class="btn btn-sm BtnGroup-item" id="raw-url">Raw</a>
        <a href="/Naetw/CTF-pwn-tips/blame/master/README.md" class="btn btn-sm js-update-url-with-hash BtnGroup-item" data-hotkey="b">Blame</a>
      <a href="/Naetw/CTF-pwn-tips/commits/master/README.md" class="btn btn-sm BtnGroup-item" rel="nofollow">History</a>
    </div>

        <a class="btn-octicon tooltipped tooltipped-nw"
           href="x-github-client://openRepo/https://github.com/Naetw/CTF-pwn-tips?branch=master&amp;filepath=README.md"
           aria-label="Open this file in GitHub Desktop"
           data-ga-click="Repository, open with desktop, type:windows">
            <svg aria-hidden="true" class="octicon octicon-device-desktop" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M15 2H1c-.55 0-1 .45-1 1v9c0 .55.45 1 1 1h5.34c-.25.61-.86 1.39-2.34 2h8c-1.48-.61-2.09-1.39-2.34-2H15c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm0 9H1V3h14v8z"/></svg>
        </a>

          <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Naetw/CTF-pwn-tips/edit/master/README.md" class="inline-form js-update-url-with-hash" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="E/IAD0poYDb690U9TH/qsR/Mo0sqK63PJq4+A960UYAXChyDh9fhdFvdXT4pchY1an0+BQgx9jhTc0dKp4FXTA==" /></div>
            <button class="btn-octicon tooltipped tooltipped-nw" type="submit"
              aria-label="Fork this project and edit the file" data-hotkey="e" data-disable-with>
              <svg aria-hidden="true" class="octicon octicon-pencil" height="16" version="1.1" viewBox="0 0 14 16" width="14"><path fill-rule="evenodd" d="M0 12v3h3l8-8-3-3-8 8zm3 2H1v-2h1v1h1v1zm10.3-9.3L12 6 9 3l1.3-1.3a.996.996 0 0 1 1.41 0l1.59 1.59c.39.39.39 1.02 0 1.41z"/></svg>
            </button>
</form>
        <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="/Naetw/CTF-pwn-tips/delete/master/README.md" class="inline-form" method="post"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /><input name="authenticity_token" type="hidden" value="vsYN94wdZ977UUcixU5ToES1TbzKahWXtYRnQfH3P9obzgh+ystqhTLSp0orErtLTDb6r/VBhiTQTVk+niegMQ==" /></div>
          <button class="btn-octicon btn-octicon-danger tooltipped tooltipped-nw" type="submit"
            aria-label="Fork this project and delete the file" data-disable-with>
            <svg aria-hidden="true" class="octicon octicon-trashcan" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M11 2H9c0-.55-.45-1-1-1H5c-.55 0-1 .45-1 1H2c-.55 0-1 .45-1 1v1c0 .55.45 1 1 1v9c0 .55.45 1 1 1h7c.55 0 1-.45 1-1V5c.55 0 1-.45 1-1V3c0-.55-.45-1-1-1zm-1 12H3V5h1v8h1V5h1v8h1V5h1v8h1V5h1v9zm1-10H2V3h9v1z"/></svg>
          </button>
</form>  </div>

  <div class="file-info">
      484 lines (344 sloc)
      <span class="file-info-divider"></span>
    16.8 KB
  </div>
</div>

    
  <div id="readme" class="readme blob instapaper_body">
    <article class="markdown-body entry-content" itemprop="text"><h1><a href="#ctf-pwn-tips" aria-hidden="true" class="anchor" id="user-content-ctf-pwn-tips"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>CTF-pwn-tips</h1>
<h1><a href="#catalog" aria-hidden="true" class="anchor" id="user-content-catalog"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Catalog</h1>
<ul>
<li><a href="#overflow">Overflow</a></li>
<li><a href="#find-string-in-gdb">Find string in gdb</a></li>
<li><a href="#binary-service">Binary Service</a></li>
<li><a href="#find-specific-function-offset-in-libc">Find specific function offset in libc</a></li>
<li><a href="#find-binsh-or-sh-in-library">Find '/bin/sh' or 'sh' in library</a></li>
<li><a href="#leak-stack-address">Leak stack address</a></li>
<li><a href="#fork-problem-in-gdb">Fork problem in gdb</a></li>
<li><a href="#secret-of-a-mysterious-section---tls">Secret of a mysterious section - .tls</a></li>
<li><a href="#predictable-rngrandom-number-generator">Predictable RNG(Random Number Generator)</a></li>
<li><a href="#make-stack-executable">Make stack executable</a></li>
<li><a href="#use-one-gadget-rce-instead-of-system">Use one-gadget-RCE instead of system</a></li>
<li><a href="#hijack-hook-function">Hijack hook function</a></li>
<li><a href="#use-printf-to-trigger-malloc-and-free">Use printf to trigger malloc and free</a></li>
<li><a href="#use-execveat-to-open-a-shell">Use execveat to open a shell</a></li>
</ul>
<h2><a href="#overflow" aria-hidden="true" class="anchor" id="user-content-overflow"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Overflow</h2>
<p>Assume that: <code>char buf[40]</code> and <code>signed int num</code></p>
<h3><a href="#scanf" aria-hidden="true" class="anchor" id="user-content-scanf"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>scanf</h3>
<ul>
<li>
<p><code>scanf("%s", buf)</code></p>
<ul>
<li><code>%s</code> doesn't have boundary check.</li>
<li><strong>pwnable</strong></li>
</ul>
</li>
<li>
<p><code>scanf("%39s", buf)</code></p>
<ul>
<li><code>%39s</code> only takes 39 bytes from the input and puts NULL byte at the end of input.</li>
<li><strong>useless</strong></li>
</ul>
</li>
<li>
<p><code>scanf("%40s", buf)</code></p>
<ul>
<li>At first sight, it seems reasonable.(seems)</li>
<li>It takes <strong>40 bytes</strong> from input, but it also <strong>puts NULL byte at the end of input.</strong></li>
<li>Therefore, it has <strong>one-byte-overflow</strong>.</li>
<li><strong>pwnable</strong></li>
</ul>
</li>
<li>
<p><code>scanf("%d", num)</code></p>
<ul>
<li>Used with <code>alloca(num)</code>
<ul>
<li>Since <code>alloca</code> allocates memory from the stack frame of the caller, there is an instruction <code>sub esp, eax</code> to achieve that.</li>
<li>If we make num negative, it will have overlapped stack frame.</li>
<li>E.g. <a href="https://github.com/ctfs/write-ups-2016/tree/master/seccon-ctf-quals-2016/exploit/cheer-msg-100">Seccon CTF quals 2016 cheer_msg</a></li>
</ul>
</li>
<li>Use num to access some data structures
<ul>
<li>In most of the time, programs only check the higher bound and forget to make num unsigned.</li>
<li>Making num negative may let us overwrite some important data to control the world!</li>
</ul>
</li>
</ul>
</li>
</ul>
<h3><a href="#gets" aria-hidden="true" class="anchor" id="user-content-gets"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gets</h3>
<ul>
<li>
<p><code>gets(buf)</code></p>
<ul>
<li>No boundary check.</li>
<li><strong>pwnable</strong></li>
</ul>
</li>
<li>
<p><code>fgets(buf, 40, stdin)</code></p>
<ul>
<li>It takes only <strong>39 bytes</strong> from the input and puts NULL byte at the end of input.</li>
<li><strong>useless</strong></li>
</ul>
</li>
</ul>
<h3><a href="#read" aria-hidden="true" class="anchor" id="user-content-read"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>read</h3>
<ul>
<li><code>read(stdin, buf, 40)</code>
<ul>
<li>It takes <strong>40 bytes</strong> from the input, and it doesn't put NULL byte at the end of input.</li>
<li>It seems safe, but it may have <strong>information leak</strong>.</li>
<li><strong>leakable</strong></li>
</ul>
</li>
</ul>
<p>E.g.</p>
<p><strong>memory layout</strong></p>
<pre><code>0x7fffffffdd00: 0x4141414141414141      0x4141414141414141
0x7fffffffdd10: 0x4141414141414141      0x4141414141414141
0x7fffffffdd20: 0x4141414141414141      0x00007fffffffe1cd
</code></pre>
<ul>
<li>
<p>If there is a <code>printf</code> or <code>puts</code> used to output the buf, it will keep outputting until reaching NULL byte.</p>
</li>
<li>
<p>In this case, we can get <code>'A'*40 + '\xcd\xe1\xff\xff\xff\x7f'</code>.</p>
</li>
<li>
<p><code>fread(stdin, buf, 1, 40)</code></p>
<ul>
<li>Almost the same as <code>read</code>.</li>
<li><strong>leakable</strong></li>
</ul>
</li>
</ul>
<h3><a href="#strcpy" aria-hidden="true" class="anchor" id="user-content-strcpy"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>strcpy</h3>
<p>Assume that there is another buffer: <code>char buf2[60]</code></p>
<ul>
<li>
<p><code>strcpy(buf, buf2)</code></p>
<ul>
<li>No boundary check.</li>
<li>It copies the content of buf2(until reaching NULL byte) which may be longer than <code>length(buf)</code> to buf.</li>
<li>Therefore, it may happen overflow.</li>
<li><strong>pwnable</strong></li>
</ul>
</li>
<li>
<p><code>strncpy(buf, buf2, 40)</code></p>
<ul>
<li>It copies 40 bytes from buf2 to buf, but it won't put NULL byte at the end.</li>
<li>Since there is no NULL byte to terminate, it may have <strong>information leak</strong>.</li>
<li><strong>leakable</strong></li>
</ul>
</li>
</ul>
<h3><a href="#strcat" aria-hidden="true" class="anchor" id="user-content-strcat"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>strcat</h3>
<p>Assume that there is another buffer: <code>char buf2[60]</code></p>
<ul>
<li>
<p><code>strcat(buf, buf2)</code></p>
<ul>
<li>Of course, it may cause <strong>overflow</strong> if <code>length(buf)</code> isn't large enough.</li>
<li>It puts NULL byte at the end, it may cause <strong>one-byte-overflow</strong>.</li>
<li>In some cases, we can use this NULL byte to change stack address or heap address.</li>
<li><strong>pwnable</strong></li>
</ul>
</li>
<li>
<p><code>strncat(buf, buf2, n)</code></p>
<ul>
<li>Almost the same as <code>strcat</code>, but with size limitation.</li>
<li><strong>pwnable</strong></li>
<li>E.g. <a href="https://github.com/ctfs/write-ups-2016/tree/master/seccon-ctf-quals-2016/exploit/jmper-300">Seccon CTF quals 2016 jmper</a></li>
</ul>
</li>
</ul>
<h2><a href="#find-string-in-gdb" aria-hidden="true" class="anchor" id="user-content-find-string-in-gdb"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Find string in gdb</h2>
<p>In the problem of <a href="http://j00ru.vexillium.org/blog/24_03_15/dragons_ctf.pdf" rel="nofollow">SSP</a>, we need to find out the offset between <code>argv[0]</code> and the input buffer.</p>
<h3><a href="#gdb" aria-hidden="true" class="anchor" id="user-content-gdb"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>gdb</h3>
<ul>
<li>Use <code>p/x ((char **)environ)</code> in gdb, and the address of argv[0] will be the <code>output - 0x10</code></li>
</ul>
<p>E.g.</p>
<pre><code>(gdb) p/x (char **)environ
$9 = 0x7fffffffde38
(gdb) x/gx 0x7fffffffde38-0x10
0x7fffffffde28: 0x00007fffffffe1cd
(gdb) x/s 0x00007fffffffe1cd
0x7fffffffe1cd: "/home/naetw/CTF/seccon2016/check/checker"
</code></pre>
<h3><a href="#gdb-peda" aria-hidden="true" class="anchor" id="user-content-gdb-peda"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a><a href="https://github.com/longld/peda">gdb peda</a></h3>
<ul>
<li>Use <code>searchmem "/home/naetw/CTF/seccon2016/check/checker"</code></li>
<li>Then use <code>searchmem $result_address</code></li>
</ul>
<pre><code>gdb-peda$ searchmem "/home/naetw/CTF/seccon2016/check/checker"
Searching for '/home/naetw/CTF/seccon2016/check/checker' in: None ranges
Found 3 results, display max 3 items:
[stack] : 0x7fffffffe1cd ("/home/naetw/CTF/seccon2016/check/checker")
[stack] : 0x7fffffffed7c ("/home/naetw/CTF/seccon2016/check/checker")
[stack] : 0x7fffffffefcf ("/home/naetw/CTF/seccon2016/check/checker")
gdb-peda$ searchmem 0x7fffffffe1cd
Searching for '0x7fffffffe1cd' in: None ranges
Found 2 results, display max 2 items:
   libc : 0x7ffff7dd33b8 --&gt; 0x7fffffffe1cd ("/home/naetw/CTF/seccon2016/check/checker")
[stack] : 0x7fffffffde28 --&gt; 0x7fffffffe1cd ("/home/naetw/CTF/seccon2016/check/checker")
</code></pre>
<h2><a href="#binary-service" aria-hidden="true" class="anchor" id="user-content-binary-service"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Binary Service</h2>
<p>Normal:</p>
<ul>
<li><code>ncat -vc ./binary -kl 127.0.0.1 $port</code></li>
</ul>
<p>With specific library in two ways:</p>
<ul>
<li><code>ncat -vc 'LD_PRELOAD=/path/to/libc.so ./binary' -kl 127.0.0.1 $port</code></li>
<li><code>ncat -vc 'LD_LIBRARY_PATH=/path/of/libc.so ./binary' -kl 127.0.0.1 $port</code></li>
</ul>
<p>After this, you can connect to binary service by command <code>nc localhost $port</code>.</p>
<h2><a href="#find-specific-function-offset-in-libc" aria-hidden="true" class="anchor" id="user-content-find-specific-function-offset-in-libc"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Find specific function offset in libc</h2>
<p>If we leaked libc address of certain function successfully, we could use get libc base address by subtracting the offset of that function.</p>
<h3><a href="#manually" aria-hidden="true" class="anchor" id="user-content-manually"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Manually</h3>
<ul>
<li><code>readelf -s $libc | grep ${function}@</code></li>
</ul>
<p>E.g.</p>
<pre><code>$ readelf -s libc-2.19.so | grep system@
    620: 00040310    56 FUNC    GLOBAL DEFAULT   12 __libc_system@@GLIBC_PRIVATE
   1443: 00040310    56 FUNC    WEAK   DEFAULT   12 system@@GLIBC_2.0
</code></pre>
<h3><a href="#automatically" aria-hidden="true" class="anchor" id="user-content-automatically"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Automatically</h3>
<ul>
<li>Use <a href="https://github.com/Gallopsled/pwntools">pwntools</a>, then you can use it in your exploit script.</li>
</ul>
<p>E.g.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> pwn <span class="pl-k">import</span> <span class="pl-k">*</span>

libc <span class="pl-k">=</span> ELF(<span class="pl-s"><span class="pl-pds">'</span>libc.so<span class="pl-pds">'</span></span>)
system_off <span class="pl-k">=</span> libc.symbols[<span class="pl-s"><span class="pl-pds">'</span>system<span class="pl-pds">'</span></span>]</pre></div>
<h2><a href="#find-binsh-or-sh-in-library" aria-hidden="true" class="anchor" id="user-content-find-binsh-or-sh-in-library"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Find '/bin/sh' or 'sh' in library</h2>
<p>Need libc base address first</p>
<h3><a href="#manually-1" aria-hidden="true" class="anchor" id="user-content-manually-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Manually</h3>
<ul>
<li><code>objdump -s libc.so | less</code> then search 'sh'</li>
<li><code>strings -tx libc.so | grep /bin/sh</code></li>
</ul>
<h3><a href="#automatically-1" aria-hidden="true" class="anchor" id="user-content-automatically-1"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Automatically</h3>
<ul>
<li>Use <a href="https://github.com/Gallopsled/pwntools">pwntools</a></li>
</ul>
<p>E.g.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">from</span> pwn <span class="pl-k">import</span> <span class="pl-k">*</span>

libc <span class="pl-k">=</span> ELF(<span class="pl-s"><span class="pl-pds">'</span>libc.so<span class="pl-pds">'</span></span>)
<span class="pl-c1">...</span>
sh <span class="pl-k">=</span> base <span class="pl-k">+</span> <span class="pl-c1">next</span>(libc.search(<span class="pl-s"><span class="pl-pds">'</span>sh<span class="pl-cce">\x00</span><span class="pl-pds">'</span></span>))
binsh <span class="pl-k">=</span> base <span class="pl-k">+</span> <span class="pl-c1">next</span>(libc.search(<span class="pl-s"><span class="pl-pds">'</span>/bin/sh<span class="pl-cce">\x00</span><span class="pl-pds">'</span></span>))</pre></div>
<h2><a href="#leak-stack-address" aria-hidden="true" class="anchor" id="user-content-leak-stack-address"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Leak stack address</h2>
<p><strong>constraints</strong>:</p>
<ul>
<li>Have already leaked libc base address</li>
<li>Can leak the content of arbitrary address</li>
</ul>
<p>There is a symbol <code>environ</code> in libc, whose value is the same as the third argument of <code>main</code> function, <code>char **envp</code>.
The value of <code>char **envp</code> is on the stack, thus we can leak stack address with this symbol.</p>
<pre><code>(gdb) list 1
1       #include &lt;stdlib.h&gt;
2       #include &lt;stdio.h&gt;
3
4       extern char **environ;
5
6       int main(int argc, char **argv, char **envp)
7       {
8           return 0;
9       }
(gdb) x/gx 0x7ffff7a0e000 + 0x3c5f38
0x7ffff7dd3f38 &lt;environ&gt;:       0x00007fffffffe230
(gdb) p/x (char **)envp
$12 = 0x7fffffffe230
</code></pre>
<ul>
<li><code>0x7ffff7a0e000</code> is current libc base address</li>
<li><code>0x3c5f38</code> is offset of <code>environ</code> in libc</li>
</ul>
<p>This <a href="https://www.gnu.org/software/libc/manual/html_node/Program-Arguments.html" rel="nofollow">manual</a> explains details about <code>environ</code>.</p>
<h2><a href="#fork-problem-in-gdb" aria-hidden="true" class="anchor" id="user-content-fork-problem-in-gdb"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Fork problem in gdb</h2>
<p>When you use <strong>gdb</strong> to debug a binary with <code>fork()</code> function, you can use the following command to determine which process to follow (The default setting of original gdb is parent, while that of gdb-peda is child.):</p>
<ul>
<li><code>set follow-fork-mode parent</code></li>
<li><code>set follow-fork-mode child</code></li>
</ul>
<p>Alternatively, using <code>set detach-on-fork off</code>, we can then control both sides of each fork. Using <code>inferior X</code> where <code>X</code> is any of the numbers that show up for <code>info inferiors</code> will switch to that side of the fork. This is useful if both sides of the fork are necessary to attack a challenge, and the simple <code>follow</code> ones above aren't sufficient.</p>
<h2><a href="#secret-of-a-mysterious-section---tls" aria-hidden="true" class="anchor" id="user-content-secret-of-a-mysterious-section---tls"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Secret of a mysterious section - .tls</h2>
<p><strong>constraints</strong>:</p>
<ul>
<li>Need <code>malloc</code> function and you can malloc with arbitrary size</li>
<li>Arbitrary address leaking</li>
</ul>
<p>We make <code>malloc</code> use <code>mmap</code> to allocate memory(size 0x21000 is enough). In general, these pages will be placed at the address just before <code>.tls</code> section.</p>
<p>There is some useful information on <strong><code>.tls</code></strong>, such as the address of <code>main_arena</code>, <code>canary</code> (value of stack guard), and a strange <code>stack address</code> which points to somewhere on the stack but with a fixed offset.</p>
<p><strong>Before calling mmap:</strong></p>
<pre><code>7fecbfe4d000-7fecbfe51000 r--p 001bd000 fd:00 131210         /lib/x86_64-linux-gnu/libc-2.24.so
7fecbfe51000-7fecbfe53000 rw-p 001c1000 fd:00 131210         /lib/x86_64-linux-gnu/libc-2.24.so
7fecbfe53000-7fecbfe57000 rw-p 00000000 00:00 0
7fecbfe57000-7fecbfe7c000 r-xp 00000000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
7fecc0068000-7fecc006a000 rw-p 00000000 00:00 0              &lt;- .tls section
7fecc0078000-7fecc007b000 rw-p 00000000 00:00 0
7fecc007b000-7fecc007c000 r--p 00024000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
7fecc007c000-7fecc007d000 rw-p 00025000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
</code></pre>
<p><strong>After call mmap:</strong></p>
<pre><code>7fecbfe4d000-7fecbfe51000 r--p 001bd000 fd:00 131210         /lib/x86_64-linux-gnu/libc-2.24.so
7fecbfe51000-7fecbfe53000 rw-p 001c1000 fd:00 131210         /lib/x86_64-linux-gnu/libc-2.24.so
7fecbfe53000-7fecbfe57000 rw-p 00000000 00:00 0
7fecbfe57000-7fecbfe7c000 r-xp 00000000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
7fecc0045000-7fecc006a000 rw-p 00000000 00:00 0              &lt;- memory of mmap + .tls section
7fecc0078000-7fecc007b000 rw-p 00000000 00:00 0
7fecc007b000-7fecc007c000 r--p 00024000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
7fecc007c000-7fecc007d000 rw-p 00025000 fd:00 131206         /lib/x86_64-linux-gnu/ld-2.24.so
</code></pre>
<h2><a href="#predictable-rngrandom-number-generator" aria-hidden="true" class="anchor" id="user-content-predictable-rngrandom-number-generator"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Predictable RNG(Random Number Generator)</h2>
<p>When the binary uses the RNG to make the address of important information or sth, we can guess the same value if it's predictable.</p>
<p>Assuming that it's predictable, we can use <a href="https://docs.python.org/2/library/ctypes.html" rel="nofollow">ctypes</a> which is a build-in module in Python.</p>
<p><strong>ctypes</strong> allows calling a function in DLL(Dynamic-Link Library) or Shared Library.</p>
<p>Therefore, if binary has an init_proc like this:</p>
<div class="highlight highlight-source-c"><pre><span class="pl-en">srand</span>(time(<span class="pl-c1">NULL</span>));
<span class="pl-k">while</span>(addr &lt;= <span class="pl-c1">0x10000</span>){
    addr = <span class="pl-c1">rand</span>() &amp; <span class="pl-c1">0xfffff000</span>;
}
secret = mmap(addr,<span class="pl-c1">0x1000</span>,PROT_READ|PROT_WRITE,MAP_PRIVATE|MAP_ANONYMOUS ,-<span class="pl-c1">1</span>,<span class="pl-c1">0</span>);
<span class="pl-k">if</span>(secret == -<span class="pl-c1">1</span>){
    <span class="pl-c1">puts</span>(<span class="pl-s"><span class="pl-pds">"</span>mmap error<span class="pl-pds">"</span></span>);
    <span class="pl-c1">exit</span>(<span class="pl-c1">0</span>);
}</pre></div>
<p>Then we can use <strong>ctypes</strong> to get the same value of addr.</p>
<div class="highlight highlight-source-python"><pre><span class="pl-k">import</span> ctypes
<span class="pl-c1">LIBC</span> <span class="pl-k">=</span> ctypes.cdll.LoadLibrary(<span class="pl-s"><span class="pl-pds">'</span>/path/to/dll<span class="pl-pds">'</span></span>)
<span class="pl-c1">LIBC</span>.srand(<span class="pl-c1">LIBC</span>.time(<span class="pl-c1">0</span>))
addr <span class="pl-k">=</span> <span class="pl-c1">LIBC</span>.rand() <span class="pl-k">&amp;</span> <span class="pl-c1"><span class="pl-k">0x</span>fffff000</span></pre></div>
<h2><a href="#make-stack-executable" aria-hidden="true" class="anchor" id="user-content-make-stack-executable"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Make stack executable</h2>
<ul>
<li><a href="http://radare.today/posts/defeating-baby_rop-with-radare2/" rel="nofollow">link1</a></li>
<li><a href="https://sploitfun.wordpress.com/author/sploitfun/" rel="nofollow">link2</a></li>
<li>Haven't read yet orz</li>
</ul>
<h2><a href="#use-one-gadget-rce-instead-of-system" aria-hidden="true" class="anchor" id="user-content-use-one-gadget-rce-instead-of-system"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use one-gadget-RCE instead of system</h2>
<p><strong>constraints</strong>:</p>
<ul>
<li>Have libc base address</li>
<li>Write to arbitrary address</li>
</ul>
<p>Almost every pwnable challenge needs to call <code>system('/bin/sh')</code> in the end of the exploit, but if we want to call that, we have to manipulate the parameters and, of course, hijack some functions to <code>system</code>. What if we <strong>can't</strong> manipulate the parameter?</p>
<p>Use <a href="http://j00ru.vexillium.org/blog/24_03_15/dragons_ctf.pdf" rel="nofollow">one-gadget-RCE</a>!</p>
<p>With <strong>one-gadget-RCE</strong>, we can just hijack <code>.got.plt</code> or something we can use to control eip to make program jump to <strong>one-gadget</strong>, but there are some constraints that need satisfying before using it.</p>
<p>There are lots of <strong>one-gadgets</strong> in libc. Each one has different constraints but those are similar. Each constraint is about the state of registers.</p>
<p>E.g.</p>
<ul>
<li>ebx is the address of <code>rw-p</code> area of libc</li>
<li>[esp+0x34] == NULL</li>
</ul>
<p>How can we get these constraints? Here is an useful tool <a href="https://github.com/david942j/one_gadget">one_gadget</a> !!!!</p>
<p>So if we can satisfy those constraints, we can get the shell more easily.</p>
<h2><a href="#hijack-hook-function" aria-hidden="true" class="anchor" id="user-content-hijack-hook-function"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Hijack hook function</h2>
<p><strong>constraints</strong>:</p>
<ul>
<li>Have libc base address</li>
<li>Write to arbitrary address</li>
<li>The program uses <code>malloc</code>, <code>free</code> or <code>realloc</code>.</li>
</ul>
<p>By manual:</p>
<blockquote>
<p>The GNU C Library lets you modify the behavior of <code>malloc</code>, <code>realloc</code>, and <code>free</code> by specifying appropriate hook functions. You can use these hooks to help you debug programs that use dynamic memory allocation, for example.</p>
</blockquote>
<p>There are hook variables declared in malloc.h and their default values are <code>0x0</code>.</p>
<ul>
<li><code>__malloc_hook</code></li>
<li><code>__free_hook</code></li>
<li>...</li>
</ul>
<p>Since they are used to help us debug programs, they are writable during the execution.</p>
<pre><code>0xf77228e0 &lt;__free_hook&gt;:       0x00000000
0xf7722000 0xf7727000 rw-p      mapped
</code></pre>
<p>Let's look into the <a href="https://code.woboq.org/userspace/glibc/malloc/malloc.c.html#2917" rel="nofollow">src</a> of malloc.c. I will use <code>__libc_free</code> to demo.</p>
<div class="highlight highlight-source-c"><pre><span class="pl-k">void</span> (*hook) (<span class="pl-k">void</span> *, <span class="pl-k">const</span> <span class="pl-k">void</span> *) = atomic_forced_read (__free_hook);
<span class="pl-k">if</span> (__builtin_expect (hook != <span class="pl-c1">NULL</span>, <span class="pl-c1">0</span>))
{
    (*hook)(mem, <span class="pl-c1">RETURN_ADDRESS</span> (<span class="pl-c1">0</span>));
    <span class="pl-k">return</span>;
}</pre></div>
<p>It checks the value of <code>__free_hook</code>. If it's not NULL, it will call the hook function first. Here, we would like to use <strong>one-gadget-RCE</strong>. Since hook function is called in the libc, the constraints of <strong>one-gadget</strong> are usually satisfied.</p>
<h2><a href="#use-printf-to-trigger-malloc-and-free" aria-hidden="true" class="anchor" id="user-content-use-printf-to-trigger-malloc-and-free"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use printf to trigger malloc and free</h2>
<p>Look into the source of printf, there are several places which may trigger malloc. Take <a href="https://code.woboq.org/userspace/glibc/stdio-common/vfprintf.c.html#1470" rel="nofollow">vfprintf.c line 1470</a> for example:</p>
<div class="highlight highlight-source-c"><pre>#<span class="pl-k">define</span> <span class="pl-en">EXTSIZ</span> <span class="pl-c1">32</span>
<span class="pl-k">enum</span> { WORK_BUFFER_SIZE = <span class="pl-c1">1000</span> };

<span class="pl-k">if</span> (width &gt;= WORK_BUFFER_SIZE - EXTSIZ)
{
    <span class="pl-c"><span class="pl-c">/*</span> We have to use a special buffer.  <span class="pl-c">*/</span></span>
    <span class="pl-c1">size_t</span> needed = ((<span class="pl-c1">size_t</span>) width + EXTSIZ) * <span class="pl-k">sizeof</span> (CHAR_T);
    <span class="pl-k">if</span> (<span class="pl-c1">__libc_use_alloca</span> (needed))
        workend = (CHAR_T *) <span class="pl-c1">alloca</span> (needed) + width + EXTSIZ;
    <span class="pl-k">else</span>
    {
        workstart = (CHAR_T *) <span class="pl-c1">malloc</span> (needed);
        <span class="pl-k">if</span> (workstart == <span class="pl-c1">NULL</span>)
        {
            done = -<span class="pl-c1">1</span>;
            <span class="pl-k">goto</span> all_done;
        }
        workend = workstart + width + EXTSIZ;
    }
}</pre></div>
<p>We can find that <code>malloc</code> will be triggered if the width field is large enough.(Of course, <code>free</code> will also be triggered at the end of printf if <code>malloc</code> has been triggered.) However, WORK_BUFFER_SIZE is not large enough, since we need to go to <strong>else</strong> block. Let's take a look at <code>__libc_use_alloca</code> and see what exactly the minimum size of width we should give.</p>
<div class="highlight highlight-source-c"><pre><span class="pl-c"><span class="pl-c">/*</span> Minimum size for a thread.  We are free to choose a reasonable value.  <span class="pl-c">*/</span></span>
#<span class="pl-k">define</span> <span class="pl-en">PTHREAD_STACK_MIN</span>        <span class="pl-c1">16384</span>

#<span class="pl-k">define</span> <span class="pl-en">__MAX_ALLOCA_CUTOFF</span>        <span class="pl-c1">65536</span>

<span class="pl-k">int</span> <span class="pl-en">__libc_use_alloca</span> (<span class="pl-c1">size_t</span> size)
{
    <span class="pl-k">return</span> (<span class="pl-c1">__builtin_expect</span> (size &lt;= PTHREAD_STACK_MIN / <span class="pl-c1">4</span>, <span class="pl-c1">1</span>)
        || <span class="pl-c1">__builtin_expect</span> (<span class="pl-c1">__libc_alloca_cutoff</span> (size), <span class="pl-c1">1</span>));
}

<span class="pl-k">int</span> <span class="pl-en">__libc_alloca_cutoff</span> (<span class="pl-c1">size_t</span> size)
{
	<span class="pl-k">return</span> size &lt;= (<span class="pl-c1">MIN</span> (__MAX_ALLOCA_CUTOFF,
					<span class="pl-c1">THREAD_GETMEM</span> (THREAD_SELF, stackblock_size) / <span class="pl-c1">4</span>
					<span class="pl-c"><span class="pl-c">/*</span> The main thread, before the thread library is</span>
<span class="pl-c">						initialized, has zero in the stackblock_size</span>
<span class="pl-c">						element.  Since it is the main thread we can</span>
<span class="pl-c">						assume the maximum available stack space.  <span class="pl-c">*/</span></span>
					?: __MAX_ALLOCA_CUTOFF * <span class="pl-c1">4</span>));
}</pre></div>
<p>We have to make sure that:</p>
<ol>
<li><code>size &gt; PTHREAD_STACK_MIN / 4</code></li>
<li><code>size &gt; MIN(__MAX_ALLOCA_CUTOFF, THREAD_GETMEM(THREAD_SELF, stackblock_size) / 4 ?: __MAX_ALLOCA_CUTOFF * 4)</code>
<ul>
<li>I did not fully understand what exactly the function - THREAD_GETMEM do, but it seems that it mostly returns 0.</li>
<li>Therefore, the second condition is usually <code>size &gt; 65536</code></li>
</ul>
</li>
</ol>
<p>More details:</p>
<ul>
<li><a href="https://gcc.gnu.org/onlinedocs/gcc/Other-Builtins.html" rel="nofollow">__builtin_expect</a></li>
<li><a href="https://code.woboq.org/userspace/glibc/sysdeps/x86_64/nptl/tls.h.html#_M/THREAD_GETMEM" rel="nofollow">THREAD_GETMEM</a></li>
</ul>
<h3><a href="#conclusion" aria-hidden="true" class="anchor" id="user-content-conclusion"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>conclusion</h3>
<ul>
<li>The minimum size of width to trigger <code>malloc</code> &amp; <code>free</code> is 65537 most of the time.</li>
<li>If there is a Format String Vulnerability and the program ends right after calling <code>printf(buf)</code>, we can hijack <code>__malloc_hook</code> or <code>__free_hook</code> with <code>one-gadget</code> and use the trick mentioned above to trigger <code>malloc</code> &amp; <code>free</code> then we can still get the shell even there is no more function call or sth after <code>printf(buf)</code>.</li>
</ul>
<h2><a href="#use-execveat-to-open-a-shell" aria-hidden="true" class="anchor" id="user-content-use-execveat-to-open-a-shell"><svg aria-hidden="true" class="octicon octicon-link" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z"></path></svg></a>Use execveat to open a shell</h2>
<p>When it comes to opening a shell with system call, <code>execve</code> always pops up in mind. However, it's not always easily available due to the lack of gadgets or others constraints.<br>
Actually, there is a system call, <code>execveat</code>, with following prototype:</p>
<div class="highlight highlight-source-c"><pre><span class="pl-k">int</span> <span class="pl-en">execveat</span>(<span class="pl-k">int</span> dirfd, <span class="pl-k">const</span> <span class="pl-k">char</span> *pathname,
             <span class="pl-k">char</span> *<span class="pl-k">const</span> argv[], <span class="pl-k">char</span> *<span class="pl-k">const</span> envp[],
             <span class="pl-k">int</span> flags);</pre></div>
<p>According to its <a href="http://man7.org/linux/man-pages/man2/execveat.2.html" rel="nofollow">man page</a>, it operates in the same way as <code>execve</code>. As for the additional arguments, it mentions that:</p>
<blockquote>
<p>If pathname is absolute, then dirfd is ignored.</p>
</blockquote>
<p>Hence, if we make <code>pathname</code> point to <code>"/bin/sh"</code>, and set <code>argv</code>, <code>envp</code> and <code>flags</code> to 0, we can still get a shell whatever the value of <code>dirfd</code>.</p>
</article>
  </div>

  </div>

  <button type="button" data-facebox="#jump-to-line" data-facebox-class="linejump" data-hotkey="l" class="d-none">Jump to Line</button>
  <div id="jump-to-line" style="display:none">
    <!-- '"` --><!-- </textarea></xmp> --></option></form><form accept-charset="UTF-8" action="" class="js-jump-to-line-form" method="get"><div style="margin:0;padding:0;display:inline"><input name="utf8" type="hidden" value="&#x2713;" /></div>
      <input class="form-control linejump-input js-jump-to-line-field" type="text" placeholder="Jump to line&hellip;" aria-label="Jump to line" autofocus>
      <button type="submit" class="btn">Go</button>
</form>  </div>


  </div>
  <div class="modal-backdrop js-touch-events"></div>
</div>

    </div>
  </div>

  </div>

      
<div class="footer container-lg px-3" role="contentinfo">
  <div class="position-relative d-flex flex-justify-between py-6 mt-6 f6 text-gray border-top border-gray-light ">
    <ul class="list-style-none d-flex flex-wrap ">
      <li class="mr-3">&copy; 2018 <span title="0.22287s from unicorn-40543988-k4cf6">GitHub</span>, Inc.</li>
        <li class="mr-3"><a href="https://github.com/site/terms" data-ga-click="Footer, go to terms, text:terms">Terms</a></li>
        <li class="mr-3"><a href="https://github.com/site/privacy" data-ga-click="Footer, go to privacy, text:privacy">Privacy</a></li>
        <li class="mr-3"><a href="https://github.com/security" data-ga-click="Footer, go to security, text:security">Security</a></li>
        <li class="mr-3"><a href="https://status.github.com/" data-ga-click="Footer, go to status, text:status">Status</a></li>
        <li><a href="https://help.github.com" data-ga-click="Footer, go to help, text:help">Help</a></li>
    </ul>

    <a href="https://github.com" aria-label="Homepage" class="footer-octicon" title="GitHub">
      <svg aria-hidden="true" class="octicon octicon-mark-github" height="24" version="1.1" viewBox="0 0 16 16" width="24"><path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0 0 16 8c0-4.42-3.58-8-8-8z"/></svg>
</a>
    <ul class="list-style-none d-flex flex-wrap ">
        <li class="mr-3"><a href="https://github.com/contact" data-ga-click="Footer, go to contact, text:contact">Contact GitHub</a></li>
      <li class="mr-3"><a href="https://developer.github.com" data-ga-click="Footer, go to api, text:api">API</a></li>
      <li class="mr-3"><a href="https://training.github.com" data-ga-click="Footer, go to training, text:training">Training</a></li>
      <li class="mr-3"><a href="https://shop.github.com" data-ga-click="Footer, go to shop, text:shop">Shop</a></li>
        <li class="mr-3"><a href="https://github.com/blog" data-ga-click="Footer, go to blog, text:blog">Blog</a></li>
        <li><a href="https://github.com/about" data-ga-click="Footer, go to about, text:about">About</a></li>

    </ul>
  </div>
</div>



  <div id="ajax-error-message" class="ajax-error-message flash flash-error">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <button type="button" class="flash-close js-ajax-error-dismiss" aria-label="Dismiss error">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
    You can't perform that action at this time.
  </div>


    
    <script crossorigin="anonymous" integrity="sha512-XMGJvyy1pIQdZi6FwfzPUDXHfItIkA7EL3jK0uSro6JSF0Tp76YxJNtflJlhbeQxOHaIj144gWd+J2ZmFUgFiQ==" src="https://assets-cdn.github.com/assets/frameworks-5cc189bf2cb5.js" type="application/javascript"></script>
    
    <script async="async" crossorigin="anonymous" integrity="sha512-aMsQNFRgVC0CvBmzYd3v297TmABZxY3vWdscdgOGJ1K6klGjK84zk+D2mQVwhmP2FLFstquNMC/97NmCYc0xrA==" src="https://assets-cdn.github.com/assets/github-68cb10345460.js" type="application/javascript"></script>
    
    
    
    
  <div class="js-stale-session-flash stale-session-flash flash flash-warn flash-banner d-none">
    <svg aria-hidden="true" class="octicon octicon-alert" height="16" version="1.1" viewBox="0 0 16 16" width="16"><path fill-rule="evenodd" d="M8.865 1.52c-.18-.31-.51-.5-.87-.5s-.69.19-.87.5L.275 13.5c-.18.31-.18.69 0 1 .19.31.52.5.87.5h13.7c.36 0 .69-.19.86-.5.17-.31.18-.69.01-1L8.865 1.52zM8.995 13h-2v-2h2v2zm0-3h-2V6h2v4z"/></svg>
    <span class="signed-in-tab-flash">You signed in with another tab or window. <a href="">Reload</a> to refresh your session.</span>
    <span class="signed-out-tab-flash">You signed out in another tab or window. <a href="">Reload</a> to refresh your session.</span>
  </div>
  <div class="facebox" id="facebox" style="display:none;">
  <div class="facebox-popup">
    <div class="facebox-content" role="dialog" aria-labelledby="facebox-header" aria-describedby="facebox-description">
    </div>
    <button type="button" class="facebox-close js-facebox-close" aria-label="Close modal">
      <svg aria-hidden="true" class="octicon octicon-x" height="16" version="1.1" viewBox="0 0 12 16" width="12"><path fill-rule="evenodd" d="M7.48 8l3.75 3.75-1.48 1.48L6 9.48l-3.75 3.75-1.48-1.48L4.52 8 .77 4.25l1.48-1.48L6 6.52l3.75-3.75 1.48 1.48z"/></svg>
    </button>
  </div>
</div>


  </body>
</html>

