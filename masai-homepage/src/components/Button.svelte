<script>
    import { Tooltip, Button } from 'flowbite-svelte';
  </script>
  
  <Button>Green tooltip</Button>
  <Tooltip color="green">Tooltip content</Tooltip>
  
  <Button>Yellow tooltip</Button>
  <Tooltip color="yellow">Tooltip content</Tooltip>
  
  <Button>Custom type</Button>
  <Tooltip placement="right" type="custom" defaultClass="" class="p-4 text-lg font-medium bg-purple-500 text-gray-100" arrow={false}>Tooltip content</Tooltip>